"""Generated from Smithy shape ``com.amazonaws.ivschat#ListRoomsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivschat.types.lambda_arn
    import aws_sdk_ivschat.types.logging_configuration_identifier
    import aws_sdk_ivschat.types.max_room_results
    import aws_sdk_ivschat.types.pagination_token
    import aws_sdk_ivschat.types.room_name


class ListRoomsRequest(TypedDict):
    name: NotRequired["aws_sdk_ivschat.types.room_name.RoomName"]
    """<p>Filters the list to match the specified room name.</p>"""
    next_token: NotRequired["aws_sdk_ivschat.types.pagination_token.PaginationToken"]
    """<p>The first room to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>"""
    max_results: NotRequired["aws_sdk_ivschat.types.max_room_results.MaxRoomResults"]
    """<p>Maximum number of rooms to return. Default: 50.</p>"""
    message_review_handler_uri: NotRequired[
        "aws_sdk_ivschat.types.lambda_arn.LambdaArn"
    ]
    """<p>Filters the list to match the specified message review handler URI.</p>"""
    logging_configuration_identifier: NotRequired[
        "aws_sdk_ivschat.types.logging_configuration_identifier.LoggingConfigurationIdentifier"
    ]
    """<p>Logging-configuration identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRoomsRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "message_review_handler_uri" in value:
        out["messageReviewHandlerUri"] = value["message_review_handler_uri"]
    if "logging_configuration_identifier" in value:
        out["loggingConfigurationIdentifier"] = value[
            "logging_configuration_identifier"
        ]
    return out


def deserialize_json(data: dict) -> ListRoomsRequest:
    out: ListRoomsRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "messageReviewHandlerUri" in data:
        out["message_review_handler_uri"] = data["messageReviewHandlerUri"]
    if "loggingConfigurationIdentifier" in data:
        out["logging_configuration_identifier"] = data["loggingConfigurationIdentifier"]
    return out
