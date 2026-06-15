"""Generated from Smithy shape ``com.amazonaws.codedeploy#AutoScalingGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.auto_scaling_group_hook
    import aws_sdk_codedeploy.types.auto_scaling_group_name


class AutoScalingGroup(TypedDict):
    name: NotRequired[
        "aws_sdk_codedeploy.types.auto_scaling_group_name.AutoScalingGroupName"
    ]
    """<p>The Auto Scaling group name.</p>"""
    hook: NotRequired[
        "aws_sdk_codedeploy.types.auto_scaling_group_hook.AutoScalingGroupHook"
    ]
    r"""<p>The name of the launch hook that CodeDeploy installed into the Auto Scaling group.</p> <p>For more information about the launch hook, see <a href=\"https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html#integrations-aws-auto-scaling-behaviors\">How Amazon EC2 Auto Scaling works with CodeDeploy</a> in the <i>CodeDeploy User Guide</i>.</p>"""
    termination_hook: NotRequired[
        "aws_sdk_codedeploy.types.auto_scaling_group_hook.AutoScalingGroupHook"
    ]
    r"""<p>The name of the termination hook that CodeDeploy installed into the Auto Scaling group.</p> <p>For more information about the termination hook, see <a href=\"https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html#integrations-aws-auto-scaling-behaviors-hook-enable\">Enabling termination deployments during Auto Scaling scale-in events</a> in the <i>CodeDeploy User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoScalingGroup) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "hook" in value:
        out["hook"] = value["hook"]
    if "termination_hook" in value:
        out["terminationHook"] = value["termination_hook"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoScalingGroup:
    out: AutoScalingGroup = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "hook" in data:
        out["hook"] = data["hook"]
    if "terminationHook" in data:
        out["termination_hook"] = data["terminationHook"]
    return out
