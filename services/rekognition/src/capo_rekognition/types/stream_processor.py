"""Generated from Smithy shape ``com.amazonaws.rekognition#StreamProcessor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.stream_processor_name
    import capo_rekognition.types.stream_processor_status


class StreamProcessor(TypedDict, closed=True):
    name: NotRequired[
        "capo_rekognition.types.stream_processor_name.StreamProcessorName"
    ]
    """<p>Name of the Amazon Rekognition stream processor. </p>"""
    status: NotRequired[
        "capo_rekognition.types.stream_processor_status.StreamProcessorStatus"
    ]
    """<p>Current status of the Amazon Rekognition stream processor.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamProcessor) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_rekognition.types.stream_processor_status

        out["Status"] = (
            capo_rekognition.types.stream_processor_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamProcessor:
    out: StreamProcessor = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import capo_rekognition.types.stream_processor_status

        out["status"] = (
            capo_rekognition.types.stream_processor_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out
