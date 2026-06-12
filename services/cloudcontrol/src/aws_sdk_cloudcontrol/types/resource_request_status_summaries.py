"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#ResourceRequestStatusSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudcontrol.types.progress_event

ResourceRequestStatusSummaries: TypeAlias = list[
    "aws_sdk_cloudcontrol.types.progress_event.ProgressEvent"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceRequestStatusSummaries) -> list:
    import aws_sdk_cloudcontrol.types.progress_event

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudcontrol.types.progress_event.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ResourceRequestStatusSummaries:
    import aws_sdk_cloudcontrol.types.progress_event

    out: ResourceRequestStatusSummaries = []
    for item in data:
        out.append(
            aws_sdk_cloudcontrol.types.progress_event.deserialize_aws_json_1_0(item)
        )
    return out
