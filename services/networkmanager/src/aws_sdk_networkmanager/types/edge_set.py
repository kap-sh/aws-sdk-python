"""Generated from Smithy shape ``com.amazonaws.networkmanager#EdgeSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.constrained_string

EdgeSet: TypeAlias = list[
    "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
]


# --- restJson1 ser/de ---
def serialize_json(value: EdgeSet) -> list:
    return list(value)


def deserialize_json(data: list) -> EdgeSet:
    return list(data)
