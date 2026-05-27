"""Generated from Smithy shape ``com.amazonaws.ecs#AutoRepairConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.auto_repair_actions_status


class AutoRepairConfiguration(TypedDict):
    actions_status: NotRequired[
        "aws_sdk_ecs.types.auto_repair_actions_status.AutoRepairActionsStatus"
    ]
    """<p>The status of auto repair actions for the capacity provider. When set to <code>ENABLED</code>, Amazon ECS automatically replaces container instances with an <code>IMPAIRED</code> health status. When set to <code>DISABLED</code>, Amazon ECS still monitors container instance health but does not automatically replace impaired instances.</p>"""
