"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyReservedInstancesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class ModifyReservedInstancesResult(TypedDict):
    reserved_instances_modification_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID for the modification.</p>"""
