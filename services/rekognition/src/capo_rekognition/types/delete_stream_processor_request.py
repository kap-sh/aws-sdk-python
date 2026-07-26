"""Generated from Smithy shape ``com.amazonaws.rekognition#DeleteStreamProcessorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.stream_processor_name


class DeleteStreamProcessorRequest(TypedDict, closed=True):
    name: "capo_rekognition.types.stream_processor_name.StreamProcessorName"
    """<p>The name of the stream processor you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteStreamProcessorRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteStreamProcessorRequest:
    out: DeleteStreamProcessorRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteStreamProcessorRequest.name required")
    return out
