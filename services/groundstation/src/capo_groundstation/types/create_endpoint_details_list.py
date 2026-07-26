"""Generated from Smithy shape ``com.amazonaws.groundstation#CreateEndpointDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_groundstation.types.create_endpoint_details

CreateEndpointDetailsList: TypeAlias = list[
    "capo_groundstation.types.create_endpoint_details.CreateEndpointDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateEndpointDetailsList) -> list:
    import capo_groundstation.types.create_endpoint_details

    out: list = []
    for item in value:
        out.append(
            capo_groundstation.types.create_endpoint_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CreateEndpointDetailsList:
    import capo_groundstation.types.create_endpoint_details

    out: CreateEndpointDetailsList = []
    for item in data:
        out.append(
            capo_groundstation.types.create_endpoint_details.deserialize_json(item)
        )
    return out
