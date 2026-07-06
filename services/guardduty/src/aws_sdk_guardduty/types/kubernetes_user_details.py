"""Generated from Smithy shape ``com.amazonaws.guardduty#KubernetesUserDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.groups
    import aws_sdk_guardduty.types.impersonated_user
    import aws_sdk_guardduty.types.session_name_list
    import aws_sdk_guardduty.types.string


class KubernetesUserDetails(TypedDict, closed=True):
    username: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The username of the user who called the Kubernetes API.</p>"""
    uid: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The user ID of the user who called the Kubernetes API.</p>"""
    groups: NotRequired["aws_sdk_guardduty.types.groups.Groups"]
    """<p>The groups that include the user who called the Kubernetes API.</p>"""
    session_name: NotRequired[
        "aws_sdk_guardduty.types.session_name_list.SessionNameList"
    ]
    """<p>Entity that assumes the IAM role when Kubernetes RBAC permissions are assigned to that role.</p>"""
    impersonated_user: NotRequired[
        "aws_sdk_guardduty.types.impersonated_user.ImpersonatedUser"
    ]
    """<p>Information about the impersonated user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesUserDetails) -> dict:
    out: dict = {}
    if "username" in value:
        out["username"] = value["username"]
    if "uid" in value:
        out["uid"] = value["uid"]
    if "groups" in value:
        import aws_sdk_guardduty.types.groups

        out["groups"] = aws_sdk_guardduty.types.groups.serialize_json(value["groups"])
    if "session_name" in value:
        import aws_sdk_guardduty.types.session_name_list

        out["sessionName"] = aws_sdk_guardduty.types.session_name_list.serialize_json(
            value["session_name"]
        )
    if "impersonated_user" in value:
        import aws_sdk_guardduty.types.impersonated_user

        out["impersonatedUser"] = (
            aws_sdk_guardduty.types.impersonated_user.serialize_json(
                value["impersonated_user"]
            )
        )
    return out


def deserialize_json(data: dict) -> KubernetesUserDetails:
    out: KubernetesUserDetails = {}  # type: ignore[typeddict-item]
    if "username" in data:
        out["username"] = data["username"]
    if "uid" in data:
        out["uid"] = data["uid"]
    if "groups" in data:
        import aws_sdk_guardduty.types.groups

        out["groups"] = aws_sdk_guardduty.types.groups.deserialize_json(data["groups"])
    if "sessionName" in data:
        import aws_sdk_guardduty.types.session_name_list

        out["session_name"] = (
            aws_sdk_guardduty.types.session_name_list.deserialize_json(
                data["sessionName"]
            )
        )
    if "impersonatedUser" in data:
        import aws_sdk_guardduty.types.impersonated_user

        out["impersonated_user"] = (
            aws_sdk_guardduty.types.impersonated_user.deserialize_json(
                data["impersonatedUser"]
            )
        )
    return out
