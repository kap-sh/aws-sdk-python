"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfIpPoolCreateRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.ip_pool_create_request

__listOfIpPoolCreateRequest: TypeAlias = list[
    "aws_sdk_medialive.types.ip_pool_create_request.IpPoolCreateRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfIpPoolCreateRequest) -> list:
    import aws_sdk_medialive.types.ip_pool_create_request

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.ip_pool_create_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfIpPoolCreateRequest:
    import aws_sdk_medialive.types.ip_pool_create_request

    out: __listOfIpPoolCreateRequest = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.ip_pool_create_request.deserialize_json(item)
        )
    return out
