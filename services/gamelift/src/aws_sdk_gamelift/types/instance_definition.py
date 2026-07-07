"""Generated from Smithy shape ``com.amazonaws.gamelift#InstanceDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_server_group_instance_type
    import aws_sdk_gamelift.types.weighted_capacity


class InstanceDefinition(TypedDict, closed=True):
    instance_type: NotRequired[
        "aws_sdk_gamelift.types.game_server_group_instance_type.GameServerGroupInstanceType"
    ]
    """<p>An Amazon EC2 instance type designation.</p>"""
    weighted_capacity: NotRequired[
        "aws_sdk_gamelift.types.weighted_capacity.WeightedCapacity"
    ]
    r"""<p>Instance weighting that indicates how much this instance type contributes to the total capacity of a game server group. Instance weights are used by Amazon GameLift Servers FleetIQ to calculate the instance type's cost per unit hour and better identify the most cost-effective options. For detailed information on weighting instance capacity, see <a href=\"https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-weighting.html\">Instance Weighting</a> in the <i>Amazon Elastic Compute Cloud Auto Scaling User Guide</i>. Default value is \"1\".</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceDefinition) -> dict:
    out: dict = {}
    if "instance_type" in value:
        import aws_sdk_gamelift.types.game_server_group_instance_type

        out["InstanceType"] = (
            aws_sdk_gamelift.types.game_server_group_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "weighted_capacity" in value:
        out["WeightedCapacity"] = value["weighted_capacity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceDefinition:
    out: InstanceDefinition = {}  # type: ignore[typeddict-item]
    if "InstanceType" in data:
        import aws_sdk_gamelift.types.game_server_group_instance_type

        out["instance_type"] = (
            aws_sdk_gamelift.types.game_server_group_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "WeightedCapacity" in data:
        out["weighted_capacity"] = data["WeightedCapacity"]
    return out
