"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ColumnNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.text

ColumnNamesList: TypeAlias = list["aws_sdk_customer_profiles.types.text.text"]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnNamesList) -> list:
    return list(value)


def deserialize_json(data: list) -> ColumnNamesList:
    return list(data)
