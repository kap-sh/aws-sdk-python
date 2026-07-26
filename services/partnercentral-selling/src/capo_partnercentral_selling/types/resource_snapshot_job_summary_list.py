"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ResourceSnapshotJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.resource_snapshot_job_summary

ResourceSnapshotJobSummaryList: TypeAlias = list[
    "capo_partnercentral_selling.types.resource_snapshot_job_summary.ResourceSnapshotJobSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceSnapshotJobSummaryList) -> list:
    import capo_partnercentral_selling.types.resource_snapshot_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.resource_snapshot_job_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ResourceSnapshotJobSummaryList:
    import capo_partnercentral_selling.types.resource_snapshot_job_summary

    out: ResourceSnapshotJobSummaryList = []
    for item in data:
        out.append(
            capo_partnercentral_selling.types.resource_snapshot_job_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
