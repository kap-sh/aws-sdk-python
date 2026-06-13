"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaStatusReason``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.schema_status_reason_code


class SchemaStatusReason(TypedDict):
    code: "aws_sdk_cleanrooms.types.schema_status_reason_code.SchemaStatusReasonCode"
    """<p>The schema status reason code.</p>"""
    message: "str"
    """<p>An explanation of the schema status reason code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaStatusReason) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.schema_status_reason_code

    out["code"] = aws_sdk_cleanrooms.types.schema_status_reason_code.serialize_json(
        value["code"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> SchemaStatusReason:
    out: SchemaStatusReason = {}  # type: ignore[typeddict-item]
    if "code" in data:
        import aws_sdk_cleanrooms.types.schema_status_reason_code

        out["code"] = (
            aws_sdk_cleanrooms.types.schema_status_reason_code.deserialize_json(
                data["code"]
            )
        )
    else:
        raise DeserializationError("SchemaStatusReason.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("SchemaStatusReason.message required")
    return out
