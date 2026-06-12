"""Generated from Smithy shape ``com.amazonaws.sagemaker#EventDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.event_metadata


class EventDetails(TypedDict):
    event_metadata: NotRequired["aws_sdk_sagemaker.types.event_metadata.EventMetadata"]
    """<p>Metadata specific to the event, which may include information about the cluster, instance group, or instance involved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventDetails) -> dict:
    out: dict = {}
    if "event_metadata" in value:
        import aws_sdk_sagemaker.types.event_metadata

        out["EventMetadata"] = (
            aws_sdk_sagemaker.types.event_metadata.serialize_aws_json_1_1(
                value["event_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EventDetails:
    out: EventDetails = {}  # type: ignore[typeddict-item]
    if "EventMetadata" in data:
        import aws_sdk_sagemaker.types.event_metadata

        out["event_metadata"] = (
            aws_sdk_sagemaker.types.event_metadata.deserialize_aws_json_1_1(
                data["EventMetadata"]
            )
        )
    return out
