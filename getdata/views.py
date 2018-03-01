from rest_framework.response import Response
from rest_framework.decorators import api_view
from chicagomap.models import *
import ast

from .models import Population
from .serializers import *


# /api/population
# GET returns entire table (domain: tract)
# POST is glorified GET but can send body for specific domains e.g. "{neighborhoods": ["Chicago Loop", "Wicker Park"]}
@api_view(['GET', 'POST'])
def population_list(request):

    if request.method == 'GET':
        serializer = PopulationSerializer(Population.objects.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        if request.data:

            body = request.data
            tracts = wards = precincts = neighborhoods = zips = []

            if 'tracts' in body.keys():
                tracts = ast.literal_eval(body['tracts'])
            if 'wards' in body.keys():
                wards = ast.literal_eval(body['wards'])
            if 'precincts' in body.keys():
                precincts = ast.literal_eval(body['precincts'])
            if 'neighborhoods' in body.keys():
                neighborhoods = ast.literal_eval(body['neighborhoods'])
            if 'zips' in body.keys():
                zips = ast.literal_eval(body['zips'])

            if tracts and not (wards or precincts or neighborhoods or zips):
                serializer = PopulationSerializer(Population.objects.filter(census_tract__name10__in=tracts), many=True)
                return Response(serializer.data)

            # figure out how to get equivalencies

        serializer = PopulationSerializer(Population.objects.all(), many=True)
        return Response(serializer.data)


