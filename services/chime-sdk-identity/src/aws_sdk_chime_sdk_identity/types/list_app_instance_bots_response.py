"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ListAppInstanceBotsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.app_instance_bot_list
    import aws_sdk_chime_sdk_identity.types.chime_arn
    import aws_sdk_chime_sdk_identity.types.next_token


class ListAppInstanceBotsResponse(TypedDict):
    app_instance_arn: NotRequired["aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"]
    """<p>The ARN of the AppInstance.</p>"""
    app_instance_bots: NotRequired[
        "aws_sdk_chime_sdk_identity.types.app_instance_bot_list.AppInstanceBotList"
    ]
    """<p>The information for each requested <code>AppInstanceBot</code>.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_identity.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested bots are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppInstanceBotsResponse) -> dict:
    out: dict = {}
    if "app_instance_arn" in value:
        out["AppInstanceArn"] = value["app_instance_arn"]
    if "app_instance_bots" in value:
        import aws_sdk_chime_sdk_identity.types.app_instance_bot_list

        out["AppInstanceBots"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_bot_list.serialize_json(
                value["app_instance_bots"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppInstanceBotsResponse:
    out: ListAppInstanceBotsResponse = {}  # type: ignore[typeddict-item]
    if "AppInstanceArn" in data:
        out["app_instance_arn"] = data["AppInstanceArn"]
    if "AppInstanceBots" in data:
        import aws_sdk_chime_sdk_identity.types.app_instance_bot_list

        out["app_instance_bots"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_bot_list.deserialize_json(
                data["AppInstanceBots"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
