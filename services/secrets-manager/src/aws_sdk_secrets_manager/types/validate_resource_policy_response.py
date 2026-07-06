"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ValidateResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.boolean_type
    import aws_sdk_secrets_manager.types.validation_errors_type


class ValidateResourcePolicyResponse(TypedDict, closed=True):
    policy_validation_passed: "aws_sdk_secrets_manager.types.boolean_type.BooleanType"
    """<p>True if your policy passes validation, otherwise false.</p>"""
    validation_errors: NotRequired[
        "aws_sdk_secrets_manager.types.validation_errors_type.ValidationErrorsType"
    ]
    """<p>Validation errors if your policy didn't pass validation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidateResourcePolicyResponse) -> dict:
    out: dict = {}
    out["PolicyValidationPassed"] = value.get("policy_validation_passed", False)
    if "validation_errors" in value:
        import aws_sdk_secrets_manager.types.validation_errors_type

        out["ValidationErrors"] = (
            aws_sdk_secrets_manager.types.validation_errors_type.serialize_aws_json_1_1(
                value["validation_errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidateResourcePolicyResponse:
    out: ValidateResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "PolicyValidationPassed" in data:
        out["policy_validation_passed"] = data["PolicyValidationPassed"]
    else:
        out["policy_validation_passed"] = False
    if "ValidationErrors" in data:
        import aws_sdk_secrets_manager.types.validation_errors_type

        out["validation_errors"] = (
            aws_sdk_secrets_manager.types.validation_errors_type.deserialize_aws_json_1_1(
                data["ValidationErrors"]
            )
        )
    return out
