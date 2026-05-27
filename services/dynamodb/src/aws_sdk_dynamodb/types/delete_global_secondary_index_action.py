"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteGlobalSecondaryIndexAction``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.index_name


class DeleteGlobalSecondaryIndexAction(TypedDict):
    index_name: "aws_sdk_dynamodb.types.index_name.IndexName"
    """<p>The name of the global secondary index to be deleted.</p>"""
