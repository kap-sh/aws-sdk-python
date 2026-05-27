"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeReservedInstancesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reserved_instances_list


class DescribeReservedInstancesResult(TypedDict):
    reserved_instances: NotRequired[
        "aws_sdk_ec2.types.reserved_instances_list.ReservedInstancesList"
    ]
    """<p>A list of Reserved Instances.</p>"""
