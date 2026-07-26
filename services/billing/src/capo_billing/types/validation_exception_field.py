"""Generated from Smithy shape ``com.amazonaws.billing#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billing.types.error_message
    import capo_billing.types.field_name


class ValidationExceptionField(TypedDict, closed=True):
    name: "capo_billing.types.field_name.FieldName"
    """<p>The name of the field.</p>"""
    message: "capo_billing.types.error_message.ErrorMessage"
    """<p>The message describing why the field failed validation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ValidationExceptionField.name required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationExceptionField.message required")
    return out
