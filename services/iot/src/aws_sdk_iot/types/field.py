"""Generated from Smithy shape ``com.amazonaws.iot#Field``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.field_name
    import aws_sdk_iot.types.field_type


class Field(TypedDict, closed=True):
    name: NotRequired["aws_sdk_iot.types.field_name.FieldName"]
    """<p>The name of the field.</p>"""
    type: NotRequired["aws_sdk_iot.types.field_type.FieldType"]
    """<p>The data type of the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Field) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import aws_sdk_iot.types.field_type

        out["type"] = aws_sdk_iot.types.field_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> Field:
    out: Field = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        import aws_sdk_iot.types.field_type

        out["type"] = aws_sdk_iot.types.field_type.deserialize_json(data["type"])
    return out
