"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfEndpointResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.endpoint_response

ListOfEndpointResponse: TypeAlias = list[
    "capo_pinpoint.types.endpoint_response.EndpointResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfEndpointResponse) -> list:
    import capo_pinpoint.types.endpoint_response

    out: list = []
    for item in value:
        out.append(capo_pinpoint.types.endpoint_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfEndpointResponse:
    import capo_pinpoint.types.endpoint_response

    out: ListOfEndpointResponse = []
    for item in data:
        out.append(capo_pinpoint.types.endpoint_response.deserialize_json(item))
    return out
