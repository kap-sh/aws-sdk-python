"""Generated from Smithy shape ``com.amazonaws.connect#QuickConnectTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.quick_connect_type

QuickConnectTypes: TypeAlias = list[
    "aws_sdk_connect.types.quick_connect_type.QuickConnectType"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuickConnectTypes) -> list:
    import aws_sdk_connect.types.quick_connect_type

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.quick_connect_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuickConnectTypes:
    import aws_sdk_connect.types.quick_connect_type

    out: QuickConnectTypes = []
    for item in data:
        out.append(aws_sdk_connect.types.quick_connect_type.deserialize_json(item))
    return out
