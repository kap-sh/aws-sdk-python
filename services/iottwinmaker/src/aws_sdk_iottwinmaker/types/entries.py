"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#Entries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.property_value_entry

Entries: TypeAlias = list[
    "aws_sdk_iottwinmaker.types.property_value_entry.PropertyValueEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: Entries) -> list:
    import aws_sdk_iottwinmaker.types.property_value_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_iottwinmaker.types.property_value_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> Entries:
    import aws_sdk_iottwinmaker.types.property_value_entry

    out: Entries = []
    for item in data:
        out.append(
            aws_sdk_iottwinmaker.types.property_value_entry.deserialize_json(item)
        )
    return out
