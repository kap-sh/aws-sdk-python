"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfApplicationResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.application_response

ListOfApplicationResponse: TypeAlias = list[
    "capo_pinpoint.types.application_response.ApplicationResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfApplicationResponse) -> list:
    import capo_pinpoint.types.application_response

    out: list = []
    for item in value:
        out.append(capo_pinpoint.types.application_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfApplicationResponse:
    import capo_pinpoint.types.application_response

    out: ListOfApplicationResponse = []
    for item in data:
        out.append(capo_pinpoint.types.application_response.deserialize_json(item))
    return out
