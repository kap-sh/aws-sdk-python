"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListEventTypesFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.list_event_types_filter

ListEventTypesFilters: TypeAlias = list[
    "aws_sdk_codestar_notifications.types.list_event_types_filter.ListEventTypesFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListEventTypesFilters) -> list:
    import aws_sdk_codestar_notifications.types.list_event_types_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codestar_notifications.types.list_event_types_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListEventTypesFilters:
    import aws_sdk_codestar_notifications.types.list_event_types_filter

    out: ListEventTypesFilters = []
    for item in data:
        out.append(
            aws_sdk_codestar_notifications.types.list_event_types_filter.deserialize_json(
                item
            )
        )
    return out
