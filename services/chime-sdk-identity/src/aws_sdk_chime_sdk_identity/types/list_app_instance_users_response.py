"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ListAppInstanceUsersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.app_instance_user_list
    import aws_sdk_chime_sdk_identity.types.chime_arn
    import aws_sdk_chime_sdk_identity.types.next_token


class ListAppInstanceUsersResponse(TypedDict, closed=True):
    app_instance_arn: NotRequired["aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"]
    """<p>The ARN of the <code>AppInstance</code>.</p>"""
    app_instance_users: NotRequired[
        "aws_sdk_chime_sdk_identity.types.app_instance_user_list.AppInstanceUserList"
    ]
    """<p>The information for each requested <code>AppInstanceUser</code>.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_identity.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested users are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppInstanceUsersResponse) -> dict:
    out: dict = {}
    if "app_instance_arn" in value:
        out["AppInstanceArn"] = value["app_instance_arn"]
    if "app_instance_users" in value:
        import aws_sdk_chime_sdk_identity.types.app_instance_user_list

        out["AppInstanceUsers"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_user_list.serialize_json(
                value["app_instance_users"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppInstanceUsersResponse:
    out: ListAppInstanceUsersResponse = {}  # type: ignore[typeddict-item]
    if "AppInstanceArn" in data:
        out["app_instance_arn"] = data["AppInstanceArn"]
    if "AppInstanceUsers" in data:
        import aws_sdk_chime_sdk_identity.types.app_instance_user_list

        out["app_instance_users"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_user_list.deserialize_json(
                data["AppInstanceUsers"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
