"""Generated from Smithy shape ``com.amazonaws.ec2#SpotFleetMonitoring``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class SpotFleetMonitoring(TypedDict):
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Enables monitoring for the instance.</p> <p>Default: <code>false</code> </p>"""
