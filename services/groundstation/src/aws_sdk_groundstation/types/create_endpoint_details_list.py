"""Generated from Smithy shape ``com.amazonaws.groundstation#CreateEndpointDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.create_endpoint_details

CreateEndpointDetailsList: TypeAlias = list[
    "aws_sdk_groundstation.types.create_endpoint_details.CreateEndpointDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateEndpointDetailsList) -> list:
    import aws_sdk_groundstation.types.create_endpoint_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_groundstation.types.create_endpoint_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CreateEndpointDetailsList:
    import aws_sdk_groundstation.types.create_endpoint_details

    out: CreateEndpointDetailsList = []
    for item in data:
        out.append(
            aws_sdk_groundstation.types.create_endpoint_details.deserialize_json(item)
        )
    return out
