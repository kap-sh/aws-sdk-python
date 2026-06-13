"""Generated from Smithy shape ``com.amazonaws.taxsettings#ValidationExceptionField``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.field_name


class ValidationExceptionField(TypedDict):
    name: "aws_sdk_taxsettings.types.field_name.FieldName"
    """<p>The name of the parameter that caused a <code>ValidationException</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ValidationExceptionField.name required")
    return out
