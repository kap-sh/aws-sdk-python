"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteReplicationGroupMemberAction``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.region_name


class DeleteReplicationGroupMemberAction(TypedDict):
    region_name: "aws_sdk_dynamodb.types.region_name.RegionName"
    """<p>The Region where the replica exists.</p>"""
