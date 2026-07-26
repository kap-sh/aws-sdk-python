"""Generated from Smithy shape ``com.amazonaws.account#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_account.types.sensitive_string


class ValidationExceptionField(TypedDict, closed=True):
    name: "str"
    """<p>The field name where the invalid entry was detected.</p>"""
    message: "capo_account.types.sensitive_string.SensitiveString"
    """<p>A message about the validation exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationExceptionField:
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
