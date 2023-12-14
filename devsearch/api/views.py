from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import ProjectSerializer
from projects.models import Project, Review, Tag


@api_view(['GET'])
def getroutes(request):

    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'GET': '/api/projects/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]
    return Response(routes)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getprojects(request):
    # print('USER', request.user)
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getproject(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectvote(request, pk):
    project = Project.object.get(id=pk)
    user = request.user.profile
    data = request.data

    review, created = Review.objects.get_or_create(
        owner=user,
        project=project,
    )

    review.value = data['value']
    review.save()
    project.getvotecount

    serializer = ProjectSerializer(project, namy=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def removetag(request):
    tagId = request.data['tag']
    projectId = request.data['project']
    project = Project.objects.get(id=projectId)
    tag = Tag.objects.get(id=tagId)
    project.tags.remove(tag)
    return Response('Tag was deleted')