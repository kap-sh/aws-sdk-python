"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#MetadataTransferJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.metadata_transfer_job_summary

MetadataTransferJobSummaries: TypeAlias = list[
    "aws_sdk_iottwinmaker.types.metadata_transfer_job_summary.MetadataTransferJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataTransferJobSummaries) -> list:
    import aws_sdk_iottwinmaker.types.metadata_transfer_job_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iottwinmaker.types.metadata_transfer_job_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MetadataTransferJobSummaries:
    import aws_sdk_iottwinmaker.types.metadata_transfer_job_summary

    out: MetadataTransferJobSummaries = []
    for item in data:
        out.append(
            aws_sdk_iottwinmaker.types.metadata_transfer_job_summary.deserialize_json(
                item
            )
        )
    return out
