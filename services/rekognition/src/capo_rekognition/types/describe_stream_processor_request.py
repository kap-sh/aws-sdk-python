"""Generated from Smithy shape ``com.amazonaws.rekognition#DescribeStreamProcessorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.stream_processor_name


class DescribeStreamProcessorRequest(TypedDict, closed=True):
    name: "capo_rekognition.types.stream_processor_name.StreamProcessorName"
    """<p>Name of the stream processor for which you want information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeStreamProcessorRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeStreamProcessorRequest:
    out: DescribeStreamProcessorRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DescribeStreamProcessorRequest.name required")
    return out
