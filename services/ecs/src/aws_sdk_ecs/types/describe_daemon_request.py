"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemonRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class DescribeDaemonRequest(TypedDict):
    daemon_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the daemon to describe.</p>"""
