"""Generated from Smithy shape ``com.amazonaws.lambda#InvokeWithResponseStreamResponseEvent``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_lambda.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.invoke_with_response_stream_complete_event
    import aws_sdk_lambda.types.invoke_response_stream_update


class _InvokeWithResponseStreamResponseEvent_PayloadChunk(TypedDict):
    PayloadChunk: (
        "aws_sdk_lambda.types.invoke_response_stream_update.InvokeResponseStreamUpdate"
    )


class _InvokeWithResponseStreamResponseEvent_InvokeComplete(TypedDict):
    InvokeComplete: "aws_sdk_lambda.types.invoke_with_response_stream_complete_event.InvokeWithResponseStreamCompleteEvent"


InvokeWithResponseStreamResponseEvent: TypeAlias = (
    _InvokeWithResponseStreamResponseEvent_PayloadChunk
    | _InvokeWithResponseStreamResponseEvent_InvokeComplete
)


# --- restJson1 ser/de ---
def serialize_json(value: InvokeWithResponseStreamResponseEvent) -> dict:
    if "PayloadChunk" in value:
        import aws_sdk_lambda.types.invoke_response_stream_update

        return {
            "PayloadChunk": aws_sdk_lambda.types.invoke_response_stream_update.serialize_json(
                value["PayloadChunk"]
            )
        }
    elif "InvokeComplete" in value:
        import aws_sdk_lambda.types.invoke_with_response_stream_complete_event

        return {
            "InvokeComplete": aws_sdk_lambda.types.invoke_with_response_stream_complete_event.serialize_json(
                value["InvokeComplete"]
            )
        }
    else:
        raise SerializationError(
            "InvokeWithResponseStreamResponseEvent: no variant present"
        )


def deserialize_json(data: dict) -> InvokeWithResponseStreamResponseEvent:
    if "PayloadChunk" in data:
        import aws_sdk_lambda.types.invoke_response_stream_update

        return {
            "PayloadChunk": aws_sdk_lambda.types.invoke_response_stream_update.deserialize_json(
                data["PayloadChunk"]
            )
        }
    elif "InvokeComplete" in data:
        import aws_sdk_lambda.types.invoke_with_response_stream_complete_event

        return {
            "InvokeComplete": aws_sdk_lambda.types.invoke_with_response_stream_complete_event.deserialize_json(
                data["InvokeComplete"]
            )
        }
    else:
        raise DeserializationError(
            "InvokeWithResponseStreamResponseEvent: no recognized variant key"
        )
