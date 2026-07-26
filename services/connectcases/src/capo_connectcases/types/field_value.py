"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.field_id
    import capo_connectcases.types.field_value_union


class FieldValue(TypedDict, closed=True):
    id: "capo_connectcases.types.field_id.FieldId"
    """<p>Unique identifier of a field.</p>"""
    value: "capo_connectcases.types.field_value_union.FieldValueUnion"
    """<p>Union of potential field value types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldValue) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_connectcases.types.field_value_union

    out["value"] = capo_connectcases.types.field_value_union.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> FieldValue:
    out: FieldValue = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("FieldValue.id required")
    if "value" in data:
        import capo_connectcases.types.field_value_union

        out["value"] = capo_connectcases.types.field_value_union.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("FieldValue.value required")
    return out
