"""Generated from Smithy shape ``com.amazonaws.groundstation#EndpointDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_groundstation.types.endpoint_details

EndpointDetailsList: TypeAlias = list[
    "capo_groundstation.types.endpoint_details.EndpointDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointDetailsList) -> list:
    import capo_groundstation.types.endpoint_details

    out: list = []
    for item in value:
        out.append(capo_groundstation.types.endpoint_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> EndpointDetailsList:
    import capo_groundstation.types.endpoint_details

    out: EndpointDetailsList = []
    for item in data:
        out.append(capo_groundstation.types.endpoint_details.deserialize_json(item))
    return out
