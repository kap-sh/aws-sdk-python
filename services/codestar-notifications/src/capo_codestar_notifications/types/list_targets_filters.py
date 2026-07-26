"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListTargetsFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codestar_notifications.types.list_targets_filter

ListTargetsFilters: TypeAlias = list[
    "capo_codestar_notifications.types.list_targets_filter.ListTargetsFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetsFilters) -> list:
    import capo_codestar_notifications.types.list_targets_filter

    out: list = []
    for item in value:
        out.append(
            capo_codestar_notifications.types.list_targets_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListTargetsFilters:
    import capo_codestar_notifications.types.list_targets_filter

    out: ListTargetsFilters = []
    for item in data:
        out.append(
            capo_codestar_notifications.types.list_targets_filter.deserialize_json(item)
        )
    return out
