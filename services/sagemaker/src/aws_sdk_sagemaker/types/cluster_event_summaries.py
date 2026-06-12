"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterEventSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_event_summary

ClusterEventSummaries: TypeAlias = list[
    "aws_sdk_sagemaker.types.cluster_event_summary.ClusterEventSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterEventSummaries) -> list:
    import aws_sdk_sagemaker.types.cluster_event_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.cluster_event_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterEventSummaries:
    import aws_sdk_sagemaker.types.cluster_event_summary

    out: ClusterEventSummaries = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.cluster_event_summary.deserialize_aws_json_1_1(item)
        )
    return out
