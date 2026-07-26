"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#UserSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service_data.types.user_summary

UserSummaryList: TypeAlias = list[
    "capo_directory_service_data.types.user_summary.UserSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserSummaryList) -> list:
    import capo_directory_service_data.types.user_summary

    out: list = []
    for item in value:
        out.append(capo_directory_service_data.types.user_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserSummaryList:
    import capo_directory_service_data.types.user_summary

    out: UserSummaryList = []
    for item in data:
        out.append(
            capo_directory_service_data.types.user_summary.deserialize_json(item)
        )
    return out
