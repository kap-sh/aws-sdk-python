"""Generated from Smithy shape ``com.amazonaws.rekognition#CreateStreamProcessorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.stream_processor_arn


class CreateStreamProcessorResponse(TypedDict, closed=True):
    stream_processor_arn: NotRequired[
        "aws_sdk_rekognition.types.stream_processor_arn.StreamProcessorArn"
    ]
    """<p>Amazon Resource Number for the newly created stream processor.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateStreamProcessorResponse) -> dict:
    out: dict = {}
    if "stream_processor_arn" in value:
        out["StreamProcessorArn"] = value["stream_processor_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateStreamProcessorResponse:
    out: CreateStreamProcessorResponse = {}  # type: ignore[typeddict-item]
    if "StreamProcessorArn" in data:
        out["stream_processor_arn"] = data["StreamProcessorArn"]
    return out
