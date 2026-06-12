"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#SampleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemakerjobruntime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemakerjobruntime.types.inference_response_body


class SampleResponse(TypedDict):
    content_type: NotRequired["str"]
    """MIME type of the inference result."""
    body: "aws_sdk_sagemakerjobruntime.types.inference_response_body.InferenceResponseBody"
    """The raw inference response body from the model."""


# --- restJson1 ser/de ---
def serialize_json(value: SampleResponse) -> dict:
    out: dict = {}
    import aws_sdk_sagemakerjobruntime.types.inference_response_body

    out["Body"] = (
        aws_sdk_sagemakerjobruntime.types.inference_response_body.serialize_json(
            value["body"]
        )
    )
    return out


def deserialize_json(data: dict) -> SampleResponse:
    out: SampleResponse = {}  # type: ignore[typeddict-item]
    if "Body" in data:
        import aws_sdk_sagemakerjobruntime.types.inference_response_body

        out["body"] = (
            aws_sdk_sagemakerjobruntime.types.inference_response_body.deserialize_json(
                data["Body"]
            )
        )
    else:
        raise DeserializationError("SampleResponse.body required")
    return out
