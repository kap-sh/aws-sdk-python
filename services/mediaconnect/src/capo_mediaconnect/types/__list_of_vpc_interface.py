"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfVpcInterface``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.vpc_interface

__listOfVpcInterface: TypeAlias = list[
    "capo_mediaconnect.types.vpc_interface.VpcInterface"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfVpcInterface) -> list:
    import capo_mediaconnect.types.vpc_interface

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.vpc_interface.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfVpcInterface:
    import capo_mediaconnect.types.vpc_interface

    out: __listOfVpcInterface = []
    for item in data:
        out.append(capo_mediaconnect.types.vpc_interface.deserialize_json(item))
    return out
