"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteGlobalTableWitnessGroupMemberAction``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.region_name


class DeleteGlobalTableWitnessGroupMemberAction(TypedDict):
    region_name: "aws_sdk_dynamodb.types.region_name.RegionName"
    """<p>The witness Region name to be removed from the MRSC global table.</p>"""
