"""Generated from Smithy shape ``com.amazonaws.ec2#TargetGroupsConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.target_groups


class TargetGroupsConfig(TypedDict):
    target_groups: NotRequired["aws_sdk_ec2.types.target_groups.TargetGroups"]
    """<p>One or more target groups.</p>"""
