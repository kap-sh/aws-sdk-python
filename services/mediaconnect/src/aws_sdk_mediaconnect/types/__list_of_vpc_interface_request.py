"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfVpcInterfaceRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.vpc_interface_request

__listOfVpcInterfaceRequest: TypeAlias = list[
    "aws_sdk_mediaconnect.types.vpc_interface_request.VpcInterfaceRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfVpcInterfaceRequest) -> list:
    import aws_sdk_mediaconnect.types.vpc_interface_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconnect.types.vpc_interface_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfVpcInterfaceRequest:
    import aws_sdk_mediaconnect.types.vpc_interface_request

    out: __listOfVpcInterfaceRequest = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.vpc_interface_request.deserialize_json(item)
        )
    return out
