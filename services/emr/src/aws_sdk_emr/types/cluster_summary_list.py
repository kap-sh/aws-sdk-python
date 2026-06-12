"""Generated from Smithy shape ``com.amazonaws.emr#ClusterSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.cluster_summary

ClusterSummaryList: TypeAlias = list["aws_sdk_emr.types.cluster_summary.ClusterSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterSummaryList) -> list:
    import aws_sdk_emr.types.cluster_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_emr.types.cluster_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterSummaryList:
    import aws_sdk_emr.types.cluster_summary

    out: ClusterSummaryList = []
    for item in data:
        out.append(aws_sdk_emr.types.cluster_summary.deserialize_aws_json_1_1(item))
    return out
