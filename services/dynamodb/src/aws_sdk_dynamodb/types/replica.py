"""Generated from Smithy shape ``com.amazonaws.dynamodb#Replica``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.region_name


class Replica(TypedDict):
    region_name: NotRequired["aws_sdk_dynamodb.types.region_name.RegionName"]
    """<p>The Region where the replica needs to be created.</p>"""
