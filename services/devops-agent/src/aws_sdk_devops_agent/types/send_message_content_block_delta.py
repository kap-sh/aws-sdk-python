"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageContentBlockDelta``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.send_message_json_delta
    import aws_sdk_devops_agent.types.send_message_text_delta


class _SendMessageContentBlockDelta_textDelta(TypedDict, closed=True):
    textDelta: "aws_sdk_devops_agent.types.send_message_text_delta.SendMessageTextDelta"


class _SendMessageContentBlockDelta_jsonDelta(TypedDict, closed=True):
    jsonDelta: "aws_sdk_devops_agent.types.send_message_json_delta.SendMessageJsonDelta"


SendMessageContentBlockDelta: TypeAlias = (
    _SendMessageContentBlockDelta_textDelta | _SendMessageContentBlockDelta_jsonDelta
)


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageContentBlockDelta) -> dict:
    if "textDelta" in value:
        import aws_sdk_devops_agent.types.send_message_text_delta

        return {
            "textDelta": aws_sdk_devops_agent.types.send_message_text_delta.serialize_json(
                value["textDelta"]
            )
        }
    elif "jsonDelta" in value:
        import aws_sdk_devops_agent.types.send_message_json_delta

        return {
            "jsonDelta": aws_sdk_devops_agent.types.send_message_json_delta.serialize_json(
                value["jsonDelta"]
            )
        }
    else:
        raise SerializationError("SendMessageContentBlockDelta: no variant present")


def deserialize_json(data: dict) -> SendMessageContentBlockDelta:
    if "textDelta" in data:
        import aws_sdk_devops_agent.types.send_message_text_delta

        return {
            "textDelta": aws_sdk_devops_agent.types.send_message_text_delta.deserialize_json(
                data["textDelta"]
            )
        }
    elif "jsonDelta" in data:
        import aws_sdk_devops_agent.types.send_message_json_delta

        return {
            "jsonDelta": aws_sdk_devops_agent.types.send_message_json_delta.deserialize_json(
                data["jsonDelta"]
            )
        }
    else:
        raise DeserializationError(
            "SendMessageContentBlockDelta: no recognized variant key"
        )
