"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.snapshot_details

SnapshotSummaries: TypeAlias = list[
    "aws_sdk_kinesis_analytics_v2.types.snapshot_details.SnapshotDetails"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotSummaries) -> list:
    import aws_sdk_kinesis_analytics_v2.types.snapshot_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.snapshot_details.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SnapshotSummaries:
    import aws_sdk_kinesis_analytics_v2.types.snapshot_details

    out: SnapshotSummaries = []
    for item in data:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.snapshot_details.deserialize_aws_json_1_1(
                item
            )
        )
    return out
