"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ValidateResourcePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.boolean_type
    import aws_sdk_secrets_manager.types.validation_errors_type


class ValidateResourcePolicyResponse(TypedDict):
    policy_validation_passed: "aws_sdk_secrets_manager.types.boolean_type.BooleanType"
    """<p>True if your policy passes validation, otherwise false.</p>"""
    validation_errors: NotRequired[
        "aws_sdk_secrets_manager.types.validation_errors_type.ValidationErrorsType"
    ]
    """<p>Validation errors if your policy didn't pass validation.</p>"""
