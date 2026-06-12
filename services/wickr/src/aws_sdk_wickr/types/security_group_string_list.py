"""Generated from Smithy shape ``com.amazonaws.wickr#SecurityGroupStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string

SecurityGroupStringList: TypeAlias = list[
    "aws_sdk_wickr.types.generic_string.GenericString"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> SecurityGroupStringList:
    return list(data)
