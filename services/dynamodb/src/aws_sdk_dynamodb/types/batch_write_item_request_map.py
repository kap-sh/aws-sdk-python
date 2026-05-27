"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchWriteItemRequestMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_arn
    import aws_sdk_dynamodb.types.write_requests

BatchWriteItemRequestMap: TypeAlias = dict[
    "aws_sdk_dynamodb.types.table_arn.TableArn",
    "aws_sdk_dynamodb.types.write_requests.WriteRequests",
]
