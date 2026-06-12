"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectionIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.connection_id

ConnectionIdList: TypeAlias = list[
    "aws_sdk_networkmanager.types.connection_id.ConnectionId"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ConnectionIdList:
    return list(data)
