"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfDescribeClusterSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.describe_cluster_summary

__listOfDescribeClusterSummary: TypeAlias = list[
    "aws_sdk_medialive.types.describe_cluster_summary.DescribeClusterSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDescribeClusterSummary) -> list:
    import aws_sdk_medialive.types.describe_cluster_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.describe_cluster_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfDescribeClusterSummary:
    import aws_sdk_medialive.types.describe_cluster_summary

    out: __listOfDescribeClusterSummary = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.describe_cluster_summary.deserialize_json(item)
        )
    return out
