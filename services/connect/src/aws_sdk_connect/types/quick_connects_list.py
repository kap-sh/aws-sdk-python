"""Generated from Smithy shape ``com.amazonaws.connect#QuickConnectsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.quick_connect_id

QuickConnectsList: TypeAlias = list[
    "aws_sdk_connect.types.quick_connect_id.QuickConnectId"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuickConnectsList) -> list:
    return list(value)


def deserialize_json(data: list) -> QuickConnectsList:
    return list(data)
