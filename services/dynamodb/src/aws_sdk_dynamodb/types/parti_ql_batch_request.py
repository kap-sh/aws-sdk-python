"""Generated from Smithy shape ``com.amazonaws.dynamodb#PartiQLBatchRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.batch_statement_request

PartiQLBatchRequest: TypeAlias = list[
    "aws_sdk_dynamodb.types.batch_statement_request.BatchStatementRequest"
]
