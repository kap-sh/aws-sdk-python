"""Generated from Smithy shape ``com.amazonaws.iot#ValidateSecurityProfileBehaviorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.valid
    import capo_iot.types.validation_errors


class ValidateSecurityProfileBehaviorsResponse(TypedDict, closed=True):
    valid: "capo_iot.types.valid.Valid"
    """<p>True if the behaviors were valid.</p>"""
    validation_errors: NotRequired["capo_iot.types.validation_errors.ValidationErrors"]
    """<p>The list of any errors found in the behaviors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateSecurityProfileBehaviorsResponse) -> dict:
    out: dict = {}
    out["valid"] = value.get("valid", False)
    if "validation_errors" in value:
        import capo_iot.types.validation_errors

        out["validationErrors"] = capo_iot.types.validation_errors.serialize_json(
            value["validation_errors"]
        )
    return out


def deserialize_json(data: dict) -> ValidateSecurityProfileBehaviorsResponse:
    out: ValidateSecurityProfileBehaviorsResponse = {}  # type: ignore[typeddict-item]
    if "valid" in data:
        out["valid"] = data["valid"]
    else:
        out["valid"] = False
    if "validationErrors" in data:
        import capo_iot.types.validation_errors

        out["validation_errors"] = capo_iot.types.validation_errors.deserialize_json(
            data["validationErrors"]
        )
    return out
