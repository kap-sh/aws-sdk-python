"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfActivityResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.activity_response

ListOfActivityResponse: TypeAlias = list[
    "capo_pinpoint.types.activity_response.ActivityResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfActivityResponse) -> list:
    import capo_pinpoint.types.activity_response

    out: list = []
    for item in value:
        out.append(capo_pinpoint.types.activity_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfActivityResponse:
    import capo_pinpoint.types.activity_response

    out: ListOfActivityResponse = []
    for item in data:
        out.append(capo_pinpoint.types.activity_response.deserialize_json(item))
    return out
