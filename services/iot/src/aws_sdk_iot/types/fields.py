"""Generated from Smithy shape ``com.amazonaws.iot#Fields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.field

Fields: TypeAlias = list["aws_sdk_iot.types.field.Field"]


# --- restJson1 ser/de ---
def serialize_json(value: Fields) -> list:
    import aws_sdk_iot.types.field

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.field.serialize_json(item))
    return out


def deserialize_json(data: list) -> Fields:
    import aws_sdk_iot.types.field

    out: Fields = []
    for item in data:
        out.append(aws_sdk_iot.types.field.deserialize_json(item))
    return out
