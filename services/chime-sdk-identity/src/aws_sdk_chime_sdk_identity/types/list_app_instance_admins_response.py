"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ListAppInstanceAdminsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.app_instance_admin_list
    import aws_sdk_chime_sdk_identity.types.chime_arn
    import aws_sdk_chime_sdk_identity.types.next_token


class ListAppInstanceAdminsResponse(TypedDict, closed=True):
    app_instance_arn: NotRequired["aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"]
    """<p>The ARN of the <code>AppInstance</code>.</p>"""
    app_instance_admins: NotRequired[
        "aws_sdk_chime_sdk_identity.types.app_instance_admin_list.AppInstanceAdminList"
    ]
    """<p>The information for each administrator.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_identity.types.next_token.NextToken"]
    """<p>The token returned from previous API requests until the number of administrators is reached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppInstanceAdminsResponse) -> dict:
    out: dict = {}
    if "app_instance_arn" in value:
        out["AppInstanceArn"] = value["app_instance_arn"]
    if "app_instance_admins" in value:
        import aws_sdk_chime_sdk_identity.types.app_instance_admin_list

        out["AppInstanceAdmins"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_admin_list.serialize_json(
                value["app_instance_admins"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppInstanceAdminsResponse:
    out: ListAppInstanceAdminsResponse = {}  # type: ignore[typeddict-item]
    if "AppInstanceArn" in data:
        out["app_instance_arn"] = data["AppInstanceArn"]
    if "AppInstanceAdmins" in data:
        import aws_sdk_chime_sdk_identity.types.app_instance_admin_list

        out["app_instance_admins"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_admin_list.deserialize_json(
                data["AppInstanceAdmins"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
