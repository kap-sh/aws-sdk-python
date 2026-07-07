"""Generated from Smithy shape ``com.amazonaws.connect#FieldValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.field_value_id
    import aws_sdk_connect.types.field_value_union


class FieldValue(TypedDict, closed=True):
    id: "aws_sdk_connect.types.field_value_id.FieldValueId"
    """<p>Unique identifier of a field.</p>"""
    value: "aws_sdk_connect.types.field_value_union.FieldValueUnion"
    """<p>Union of potential field value types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldValue) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import aws_sdk_connect.types.field_value_union

    out["Value"] = aws_sdk_connect.types.field_value_union.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> FieldValue:
    out: FieldValue = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("FieldValue.id required")
    if "Value" in data:
        import aws_sdk_connect.types.field_value_union

        out["value"] = aws_sdk_connect.types.field_value_union.deserialize_json(
            data["Value"]
        )
    else:
        raise DeserializationError("FieldValue.value required")
    return out
