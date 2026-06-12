"""Generated from Smithy shape ``com.amazonaws.networkmanager#PeeringErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.peering_error

PeeringErrorList: TypeAlias = list[
    "aws_sdk_networkmanager.types.peering_error.PeeringError"
]


# --- restJson1 ser/de ---
def serialize_json(value: PeeringErrorList) -> list:
    import aws_sdk_networkmanager.types.peering_error

    out: list = []
    for item in value:
        out.append(aws_sdk_networkmanager.types.peering_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> PeeringErrorList:
    import aws_sdk_networkmanager.types.peering_error

    out: PeeringErrorList = []
    for item in data:
        out.append(aws_sdk_networkmanager.types.peering_error.deserialize_json(item))
    return out
