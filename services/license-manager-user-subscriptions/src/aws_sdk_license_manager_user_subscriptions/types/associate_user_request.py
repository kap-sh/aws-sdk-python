"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#AssociateUserRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_license_manager_user_subscriptions.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.identity_provider
    import aws_sdk_license_manager_user_subscriptions.types.tags

class AssociateUserRequest(TypedDict):
    username: "str"
    """<p>The user name from the identity provider.</p>"""
    instance_id: "str"
    """<p>The ID of the EC2 instance that provides the user-based subscription.</p>"""
    identity_provider: "aws_sdk_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"
    """<p>The identity provider for the user.</p>"""
    domain: NotRequired["str"]
    """<p>The domain name of the Active Directory that contains information for the user to associate.</p>"""
    tags: NotRequired["aws_sdk_license_manager_user_subscriptions.types.tags.Tags"]
    """<p>The tags that apply for the user association.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AssociateUserRequest) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    out["InstanceId"] = value["instance_id"]
    import aws_sdk_license_manager_user_subscriptions.types.identity_provider
    out["IdentityProvider"] = aws_sdk_license_manager_user_subscriptions.types.identity_provider.serialize_json(value["identity_provider"])
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "tags" in value:
        import aws_sdk_license_manager_user_subscriptions.types.tags
        out["Tags"] = aws_sdk_license_manager_user_subscriptions.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AssociateUserRequest:
    out: AssociateUserRequest = {}  # type: ignore[typeddict-item]
    if "Username" in data:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("AssociateUserRequest.username required")
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("AssociateUserRequest.instance_id required")
    if "IdentityProvider" in data:
        import aws_sdk_license_manager_user_subscriptions.types.identity_provider
        out["identity_provider"] = aws_sdk_license_manager_user_subscriptions.types.identity_provider.deserialize_json(data["IdentityProvider"])
    else:
        raise DeserializationError("AssociateUserRequest.identity_provider required")
    if "Domain" in data:
        out["domain"] = data["Domain"]
    if "Tags" in data:
        import aws_sdk_license_manager_user_subscriptions.types.tags
        out["tags"] = aws_sdk_license_manager_user_subscriptions.types.tags.deserialize_json(data["Tags"])
    return out