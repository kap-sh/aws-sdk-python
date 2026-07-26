"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaStatusReason``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.schema_status_reason_code


class SchemaStatusReason(TypedDict, closed=True):
    code: "capo_cleanrooms.types.schema_status_reason_code.SchemaStatusReasonCode"
    """<p>The schema status reason code.</p>"""
    message: "str"
    """<p>An explanation of the schema status reason code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaStatusReason) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.schema_status_reason_code

    out["code"] = capo_cleanrooms.types.schema_status_reason_code.serialize_json(
        value["code"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> SchemaStatusReason:
    out: SchemaStatusReason = {}  # type: ignore[typeddict-item]
    if "code" in data:
        import capo_cleanrooms.types.schema_status_reason_code

        out["code"] = capo_cleanrooms.types.schema_status_reason_code.deserialize_json(
            data["code"]
        )
    else:
        raise DeserializationError("SchemaStatusReason.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("SchemaStatusReason.message required")
    return out
