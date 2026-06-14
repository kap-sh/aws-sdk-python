"""Generated from Smithy shape ``com.amazonaws.appintegrations#FieldsList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.fields

FieldsList: TypeAlias = list["aws_sdk_appintegrations.types.fields.Fields"]


# --- restJson1 ser/de ---
def serialize_json(value: FieldsList) -> list:
    return list(value)


def deserialize_json(data: list) -> FieldsList:
    return list(data)