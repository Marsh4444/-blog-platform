from .models import RoleRequest

def role_request_status(request):
    pending_request = None
    if request.user.is_authenticated:
        pending_request = RoleRequest.objects.filter(
            user=request.user, status="Pending"
        ).first()
    return {"pending_request": pending_request}