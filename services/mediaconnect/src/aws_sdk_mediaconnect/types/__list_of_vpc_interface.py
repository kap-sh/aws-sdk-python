"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfVpcInterface``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.vpc_interface

__listOfVpcInterface: TypeAlias = list[
    "aws_sdk_mediaconnect.types.vpc_interface.VpcInterface"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfVpcInterface) -> list:
    import aws_sdk_mediaconnect.types.vpc_interface

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconnect.types.vpc_interface.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfVpcInterface:
    import aws_sdk_mediaconnect.types.vpc_interface

    out: __listOfVpcInterface = []
    for item in data:
        out.append(aws_sdk_mediaconnect.types.vpc_interface.deserialize_json(item))
    return out
