"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#RequestStreamEvent``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_sagemaker_runtime_http2.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_sagemaker_runtime_http2.types.request_payload_part


class _RequestStreamEvent_PayloadPart(TypedDict):
    PayloadPart: (
        "aws_sdk_sagemaker_runtime_http2.types.request_payload_part.RequestPayloadPart"
    )


RequestStreamEvent: TypeAlias = _RequestStreamEvent_PayloadPart


# --- restJson1 ser/de ---
def serialize_json(value: RequestStreamEvent) -> dict:
    if "PayloadPart" in value:
        import aws_sdk_sagemaker_runtime_http2.types.request_payload_part

        return {
            "PayloadPart": aws_sdk_sagemaker_runtime_http2.types.request_payload_part.serialize_json(
                value["PayloadPart"]
            )
        }
    else:
        raise SerializationError("RequestStreamEvent: no variant present")


def deserialize_json(data: dict) -> RequestStreamEvent:
    if "PayloadPart" in data:
        import aws_sdk_sagemaker_runtime_http2.types.request_payload_part

        return {
            "PayloadPart": aws_sdk_sagemaker_runtime_http2.types.request_payload_part.deserialize_json(
                data["PayloadPart"]
            )
        }
    else:
        raise DeserializationError("RequestStreamEvent: no recognized variant key")
