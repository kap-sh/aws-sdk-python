"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SourceFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.string_to2048

SourceFields: TypeAlias = list[
    "aws_sdk_customer_profiles.types.string_to2048.stringTo2048"
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceFields) -> list:
    return list(value)


def deserialize_json(data: list) -> SourceFields:
    return list(data)
