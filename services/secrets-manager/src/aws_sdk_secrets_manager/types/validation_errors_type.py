"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ValidationErrorsType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.validation_errors_entry

ValidationErrorsType: TypeAlias = list[
    "aws_sdk_secrets_manager.types.validation_errors_entry.ValidationErrorsEntry"
]
