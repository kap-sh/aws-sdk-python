"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ValidationError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.field_map


class ValidationError(TypedDict):
    message: NotRequired["str"]
    """<p>The error message describing the validation issue.</p>"""
    reason: NotRequired["str"]
    """<p>The reason code or category for the validation error.</p>"""
    field_map: NotRequired["aws_sdk_observabilityadmin.types.field_map.FieldMap"]
    """<p>A mapping of field names to specific validation issues within the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationError) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    if "field_map" in value:
        import aws_sdk_observabilityadmin.types.field_map

        out["FieldMap"] = aws_sdk_observabilityadmin.types.field_map.serialize_json(
            value["field_map"]
        )
    return out


def deserialize_json(data: dict) -> ValidationError:
    out: ValidationError = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        out["reason"] = data["Reason"]
    if "FieldMap" in data:
        import aws_sdk_observabilityadmin.types.field_map

        out["field_map"] = aws_sdk_observabilityadmin.types.field_map.deserialize_json(
            data["FieldMap"]
        )
    return out
