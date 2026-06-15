"""Generated from Smithy shape ``com.amazonaws.ivschat#CreateRoomRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivschat.types.logging_configuration_identifier_list
    import aws_sdk_ivschat.types.message_review_handler
    import aws_sdk_ivschat.types.room_max_message_length
    import aws_sdk_ivschat.types.room_max_message_rate_per_second
    import aws_sdk_ivschat.types.room_name
    import aws_sdk_ivschat.types.tags


class CreateRoomRequest(TypedDict):
    name: NotRequired["aws_sdk_ivschat.types.room_name.RoomName"]
    """<p>Room name. The value does not need to be unique.</p>"""
    maximum_message_rate_per_second: NotRequired[
        "aws_sdk_ivschat.types.room_max_message_rate_per_second.RoomMaxMessageRatePerSecond"
    ]
    """<p>Maximum number of messages per second that can be sent to the room (by all clients). Default: 10. </p>"""
    maximum_message_length: NotRequired[
        "aws_sdk_ivschat.types.room_max_message_length.RoomMaxMessageLength"
    ]
    """<p>Maximum number of characters in a single message. Messages are expected to be UTF-8 encoded and this limit applies specifically to rune/code-point count, not number of bytes. Default: 500.</p>"""
    message_review_handler: NotRequired[
        "aws_sdk_ivschat.types.message_review_handler.MessageReviewHandler"
    ]
    """<p>Configuration information for optional review of messages.</p>"""
    tags: NotRequired["aws_sdk_ivschat.types.tags.Tags"]
    r"""<p>Tags to attach to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS Chat has no constraints beyond what is documented there.</p>"""
    logging_configuration_identifiers: NotRequired[
        "aws_sdk_ivschat.types.logging_configuration_identifier_list.LoggingConfigurationIdentifierList"
    ]
    """<p>Array of logging-configuration identifiers attached to the room.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRoomRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "maximum_message_rate_per_second" in value:
        out["maximumMessageRatePerSecond"] = value["maximum_message_rate_per_second"]
    if "maximum_message_length" in value:
        out["maximumMessageLength"] = value["maximum_message_length"]
    if "message_review_handler" in value:
        import aws_sdk_ivschat.types.message_review_handler

        out["messageReviewHandler"] = (
            aws_sdk_ivschat.types.message_review_handler.serialize_json(
                value["message_review_handler"]
            )
        )
    if "tags" in value:
        import aws_sdk_ivschat.types.tags

        out["tags"] = aws_sdk_ivschat.types.tags.serialize_json(value["tags"])
    if "logging_configuration_identifiers" in value:
        import aws_sdk_ivschat.types.logging_configuration_identifier_list

        out["loggingConfigurationIdentifiers"] = (
            aws_sdk_ivschat.types.logging_configuration_identifier_list.serialize_json(
                value["logging_configuration_identifiers"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateRoomRequest:
    out: CreateRoomRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "maximumMessageRatePerSecond" in data:
        out["maximum_message_rate_per_second"] = data["maximumMessageRatePerSecond"]
    if "maximumMessageLength" in data:
        out["maximum_message_length"] = data["maximumMessageLength"]
    if "messageReviewHandler" in data:
        import aws_sdk_ivschat.types.message_review_handler

        out["message_review_handler"] = (
            aws_sdk_ivschat.types.message_review_handler.deserialize_json(
                data["messageReviewHandler"]
            )
        )
    if "tags" in data:
        import aws_sdk_ivschat.types.tags

        out["tags"] = aws_sdk_ivschat.types.tags.deserialize_json(data["tags"])
    if "loggingConfigurationIdentifiers" in data:
        import aws_sdk_ivschat.types.logging_configuration_identifier_list

        out["logging_configuration_identifiers"] = (
            aws_sdk_ivschat.types.logging_configuration_identifier_list.deserialize_json(
                data["loggingConfigurationIdentifiers"]
            )
        )
    return out
