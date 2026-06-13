"""Generated from Smithy shape ``com.amazonaws.location#ListRouteCalculatorsResponseEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.list_route_calculators_response_entry

ListRouteCalculatorsResponseEntryList: TypeAlias = list[
    "aws_sdk_location.types.list_route_calculators_response_entry.ListRouteCalculatorsResponseEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListRouteCalculatorsResponseEntryList) -> list:
    import aws_sdk_location.types.list_route_calculators_response_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_location.types.list_route_calculators_response_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListRouteCalculatorsResponseEntryList:
    import aws_sdk_location.types.list_route_calculators_response_entry

    out: ListRouteCalculatorsResponseEntryList = []
    for item in data:
        out.append(
            aws_sdk_location.types.list_route_calculators_response_entry.deserialize_json(
                item
            )
        )
    return out
