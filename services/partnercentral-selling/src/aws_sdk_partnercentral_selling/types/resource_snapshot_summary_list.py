"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ResourceSnapshotSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.resource_snapshot_summary

ResourceSnapshotSummaryList: TypeAlias = list[
    "aws_sdk_partnercentral_selling.types.resource_snapshot_summary.ResourceSnapshotSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceSnapshotSummaryList) -> list:
    import aws_sdk_partnercentral_selling.types.resource_snapshot_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_selling.types.resource_snapshot_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ResourceSnapshotSummaryList:
    import aws_sdk_partnercentral_selling.types.resource_snapshot_summary

    out: ResourceSnapshotSummaryList = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_selling.types.resource_snapshot_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
