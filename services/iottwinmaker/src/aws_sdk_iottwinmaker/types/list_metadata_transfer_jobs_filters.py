"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListMetadataTransferJobsFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.list_metadata_transfer_jobs_filter

ListMetadataTransferJobsFilters: TypeAlias = list[
    "aws_sdk_iottwinmaker.types.list_metadata_transfer_jobs_filter.ListMetadataTransferJobsFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListMetadataTransferJobsFilters) -> list:
    import aws_sdk_iottwinmaker.types.list_metadata_transfer_jobs_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iottwinmaker.types.list_metadata_transfer_jobs_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListMetadataTransferJobsFilters:
    import aws_sdk_iottwinmaker.types.list_metadata_transfer_jobs_filter

    out: ListMetadataTransferJobsFilters = []
    for item in data:
        out.append(
            aws_sdk_iottwinmaker.types.list_metadata_transfer_jobs_filter.deserialize_json(
                item
            )
        )
    return out
