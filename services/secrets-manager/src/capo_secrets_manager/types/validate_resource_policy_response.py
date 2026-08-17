"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ValidateResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.boolean_type
    import capo_secrets_manager.types.validation_errors_type


class ValidateResourcePolicyResponse(TypedDict, closed=True):
    policy_validation_passed: "capo_secrets_manager.types.boolean_type.BooleanType"
    """<p>True if your policy passes validation, otherwise false.</p>"""
    validation_errors: NotRequired[
        "capo_secrets_manager.types.validation_errors_type.ValidationErrorsType"
    ]
    """<p>Validation errors if your policy didn't pass validation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidateResourcePolicyResponse) -> dict:
    out: dict = {}
    out["PolicyValidationPassed"] = value.get("policy_validation_passed", False)
    if "validation_errors" in value:
        import capo_secrets_manager.types.validation_errors_type

        out["ValidationErrors"] = (
            capo_secrets_manager.types.validation_errors_type.serialize_aws_json_1_1(
                value["validation_errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidateResourcePolicyResponse:
    out: ValidateResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("PolicyValidationPassed") is not None:
        out["policy_validation_passed"] = data["PolicyValidationPassed"]
    else:
        out["policy_validation_passed"] = False
    if data.get("ValidationErrors") is not None:
        import capo_secrets_manager.types.validation_errors_type

        out["validation_errors"] = (
            capo_secrets_manager.types.validation_errors_type.deserialize_aws_json_1_1(
                data["ValidationErrors"]
            )
        )
    return out
