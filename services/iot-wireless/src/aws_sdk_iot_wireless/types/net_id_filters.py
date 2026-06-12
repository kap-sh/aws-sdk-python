"""Generated from Smithy shape ``com.amazonaws.iotwireless#NetIdFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.net_id

NetIdFilters: TypeAlias = list["aws_sdk_iot_wireless.types.net_id.NetId"]


# --- restJson1 ser/de ---
def serialize_json(value: NetIdFilters) -> list:
    return list(value)


def deserialize_json(data: list) -> NetIdFilters:
    return list(data)
