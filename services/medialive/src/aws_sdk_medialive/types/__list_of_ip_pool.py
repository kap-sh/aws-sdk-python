"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfIpPool``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.ip_pool

__listOfIpPool: TypeAlias = list["aws_sdk_medialive.types.ip_pool.IpPool"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfIpPool) -> list:
    import aws_sdk_medialive.types.ip_pool

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.ip_pool.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfIpPool:
    import aws_sdk_medialive.types.ip_pool

    out: __listOfIpPool = []
    for item in data:
        out.append(aws_sdk_medialive.types.ip_pool.deserialize_json(item))
    return out
