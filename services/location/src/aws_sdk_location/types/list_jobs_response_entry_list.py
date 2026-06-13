"""Generated from Smithy shape ``com.amazonaws.location#ListJobsResponseEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.list_jobs_response_entry

ListJobsResponseEntryList: TypeAlias = list[
    "aws_sdk_location.types.list_jobs_response_entry.ListJobsResponseEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsResponseEntryList) -> list:
    import aws_sdk_location.types.list_jobs_response_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_location.types.list_jobs_response_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListJobsResponseEntryList:
    import aws_sdk_location.types.list_jobs_response_entry

    out: ListJobsResponseEntryList = []
    for item in data:
        out.append(
            aws_sdk_location.types.list_jobs_response_entry.deserialize_json(item)
        )
    return out
