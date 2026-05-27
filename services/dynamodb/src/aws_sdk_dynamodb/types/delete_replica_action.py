"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteReplicaAction``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.region_name


class DeleteReplicaAction(TypedDict):
    region_name: "aws_sdk_dynamodb.types.region_name.RegionName"
    """<p>The Region of the replica to be removed.</p>"""
