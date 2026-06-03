"""Generated from Smithy shape ``com.amazonaws.secretsmanager#FilterValuesStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.filter_value_string_type

FilterValuesStringList: TypeAlias = list[
    "aws_sdk_secrets_manager.types.filter_value_string_type.FilterValueStringType"
]
