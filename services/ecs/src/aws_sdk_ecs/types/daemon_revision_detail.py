"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonRevisionDetail``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_capacity_provider_list
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.string


class DaemonRevisionDetail(TypedDict):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon revision.</p>"""
    capacity_providers: NotRequired[
        "aws_sdk_ecs.types.daemon_capacity_provider_list.DaemonCapacityProviderList"
    ]
    """<p>The capacity providers associated with this daemon revision.</p>"""
    total_running_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The total number of daemon tasks running for this revision.</p>"""
