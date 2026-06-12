"""Generated from Smithy shape ``com.amazonaws.rekognition#StopStreamProcessorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.stream_processor_name


class StopStreamProcessorRequest(TypedDict):
    name: "aws_sdk_rekognition.types.stream_processor_name.StreamProcessorName"
    """<p>The name of a stream processor created by <a>CreateStreamProcessor</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopStreamProcessorRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopStreamProcessorRequest:
    out: StopStreamProcessorRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("StopStreamProcessorRequest.name required")
    return out
