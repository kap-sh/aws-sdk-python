"""Generated from Smithy shape ``com.amazonaws.ec2#EfaInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.maximum_efa_interfaces


class EfaInfo(TypedDict):
    maximum_efa_interfaces: NotRequired[
        "aws_sdk_ec2.types.maximum_efa_interfaces.MaximumEfaInterfaces"
    ]
    """<p>The maximum number of Elastic Fabric Adapters for the instance type.</p>"""
