"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedAutoScaling``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.managed_application_auto_scaling_policies
    import aws_sdk_ecs.types.managed_scalable_target


class ManagedAutoScaling(TypedDict):
    scalable_target: NotRequired[
        "aws_sdk_ecs.types.managed_scalable_target.ManagedScalableTarget"
    ]
    """<p>Represents a scalable target.</p>"""
    application_auto_scaling_policies: NotRequired[
        "aws_sdk_ecs.types.managed_application_auto_scaling_policies.ManagedApplicationAutoScalingPolicies"
    ]
    """<p>The policy used for auto scaling.</p>"""
