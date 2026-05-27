"""Generated from Smithy shape ``com.amazonaws.dynamodb#PartiQLBatchResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.batch_statement_response

PartiQLBatchResponse: TypeAlias = list[
    "aws_sdk_dynamodb.types.batch_statement_response.BatchStatementResponse"
]
