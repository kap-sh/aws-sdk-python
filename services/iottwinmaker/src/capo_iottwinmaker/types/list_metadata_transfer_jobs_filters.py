"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListMetadataTransferJobsFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.list_metadata_transfer_jobs_filter

ListMetadataTransferJobsFilters: TypeAlias = list[
    "capo_iottwinmaker.types.list_metadata_transfer_jobs_filter.ListMetadataTransferJobsFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListMetadataTransferJobsFilters) -> list:
    import capo_iottwinmaker.types.list_metadata_transfer_jobs_filter

    out: list = []
    for item in value:
        out.append(
            capo_iottwinmaker.types.list_metadata_transfer_jobs_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListMetadataTransferJobsFilters:
    import capo_iottwinmaker.types.list_metadata_transfer_jobs_filter

    out: ListMetadataTransferJobsFilters = []
    for item in data:
        out.append(
            capo_iottwinmaker.types.list_metadata_transfer_jobs_filter.deserialize_json(
                item
            )
        )
    return out
