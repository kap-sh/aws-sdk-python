"""Generated from Smithy shape ``com.amazonaws.dynamodb#ParameterizedStatements``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.parameterized_statement

ParameterizedStatements: TypeAlias = list[
    "aws_sdk_dynamodb.types.parameterized_statement.ParameterizedStatement"
]
