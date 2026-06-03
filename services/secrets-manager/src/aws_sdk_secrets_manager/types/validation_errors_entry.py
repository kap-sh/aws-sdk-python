"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ValidationErrorsEntry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.error_message
    import aws_sdk_secrets_manager.types.name_type


class ValidationErrorsEntry(TypedDict):
    check_name: NotRequired["aws_sdk_secrets_manager.types.name_type.NameType"]
    """<p>Checks the name of the policy.</p>"""
    error_message: NotRequired[
        "aws_sdk_secrets_manager.types.error_message.ErrorMessage"
    ]
    """<p>Displays error messages if validation encounters problems during validation of the resource policy.</p>"""
