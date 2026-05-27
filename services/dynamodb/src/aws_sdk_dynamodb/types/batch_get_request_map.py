"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchGetRequestMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_arn
    import aws_sdk_dynamodb.types.keys_and_attributes

BatchGetRequestMap: TypeAlias = dict[
    "aws_sdk_dynamodb.types.table_arn.TableArn",
    "aws_sdk_dynamodb.types.keys_and_attributes.KeysAndAttributes",
]
