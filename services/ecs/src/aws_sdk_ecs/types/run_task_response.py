"""Generated from Smithy shape ``com.amazonaws.ecs#RunTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.failures
    import aws_sdk_ecs.types.tasks


class RunTaskResponse(TypedDict):
    tasks: NotRequired["aws_sdk_ecs.types.tasks.Tasks"]
    """<p>A full description of the tasks that were run. The tasks that were successfully placed on your cluster are described here.</p>"""
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p> <p>For information about how to address failures, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages.html#service-event-messages-list\">Service event messages</a> and <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/api_failures_messages.html\">API failure reasons</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
