"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#GroupSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service_data.types.group_summary

GroupSummaryList: TypeAlias = list[
    "capo_directory_service_data.types.group_summary.GroupSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupSummaryList) -> list:
    import capo_directory_service_data.types.group_summary

    out: list = []
    for item in value:
        out.append(capo_directory_service_data.types.group_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupSummaryList:
    import capo_directory_service_data.types.group_summary

    out: GroupSummaryList = []
    for item in data:
        out.append(
            capo_directory_service_data.types.group_summary.deserialize_json(item)
        )
    return out
