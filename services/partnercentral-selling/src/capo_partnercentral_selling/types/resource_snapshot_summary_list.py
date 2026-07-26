"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ResourceSnapshotSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.resource_snapshot_summary

ResourceSnapshotSummaryList: TypeAlias = list[
    "capo_partnercentral_selling.types.resource_snapshot_summary.ResourceSnapshotSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceSnapshotSummaryList) -> list:
    import capo_partnercentral_selling.types.resource_snapshot_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.resource_snapshot_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ResourceSnapshotSummaryList:
    import capo_partnercentral_selling.types.resource_snapshot_summary

    out: ResourceSnapshotSummaryList = []
    for item in data:
        out.append(
            capo_partnercentral_selling.types.resource_snapshot_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
