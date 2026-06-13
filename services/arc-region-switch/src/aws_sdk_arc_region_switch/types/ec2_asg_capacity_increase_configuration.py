"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Ec2AsgCapacityIncreaseConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.asg_list
    import aws_sdk_arc_region_switch.types.ec2_asg_capacity_monitoring_approach
    import aws_sdk_arc_region_switch.types.ec2_ungraceful


class Ec2AsgCapacityIncreaseConfiguration(TypedDict):
    timeout_minutes: "int"
    """<p>The timeout value specified for the configuration.</p>"""
    asgs: "aws_sdk_arc_region_switch.types.asg_list.AsgList"
    """<p>The EC2 Auto Scaling groups for the configuration.</p>"""
    ungraceful: NotRequired[
        "aws_sdk_arc_region_switch.types.ec2_ungraceful.Ec2Ungraceful"
    ]
    """<p>The settings for ungraceful execution.</p>"""
    target_percent: "int"
    """<p>The target percentage that you specify for EC2 Auto Scaling groups. The default is 100.</p>"""
    capacity_monitoring_approach: "aws_sdk_arc_region_switch.types.ec2_asg_capacity_monitoring_approach.Ec2AsgCapacityMonitoringApproach"
    """<p>The monitoring approach that you specify EC2 Auto Scaling groups for the configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Ec2AsgCapacityIncreaseConfiguration) -> dict:
    out: dict = {}
    out["timeoutMinutes"] = value.get("timeout_minutes", 60)
    import aws_sdk_arc_region_switch.types.asg_list

    out["asgs"] = aws_sdk_arc_region_switch.types.asg_list.serialize_aws_json_1_0(
        value["asgs"]
    )
    if "ungraceful" in value:
        import aws_sdk_arc_region_switch.types.ec2_ungraceful

        out["ungraceful"] = (
            aws_sdk_arc_region_switch.types.ec2_ungraceful.serialize_aws_json_1_0(
                value["ungraceful"]
            )
        )
    out["targetPercent"] = value.get("target_percent", 100)
    import aws_sdk_arc_region_switch.types.ec2_asg_capacity_monitoring_approach

    out["capacityMonitoringApproach"] = (
        aws_sdk_arc_region_switch.types.ec2_asg_capacity_monitoring_approach.serialize_aws_json_1_0(
            value.get("capacity_monitoring_approach", "sampledMaxInLast24Hours")
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> Ec2AsgCapacityIncreaseConfiguration:
    out: Ec2AsgCapacityIncreaseConfiguration = {}  # type: ignore[typeddict-item]
    if "timeoutMinutes" in data:
        out["timeout_minutes"] = data["timeoutMinutes"]
    else:
        out["timeout_minutes"] = 60
    if "asgs" in data:
        import aws_sdk_arc_region_switch.types.asg_list

        out["asgs"] = aws_sdk_arc_region_switch.types.asg_list.deserialize_aws_json_1_0(
            data["asgs"]
        )
    else:
        raise DeserializationError("Ec2AsgCapacityIncreaseConfiguration.asgs required")
    if "ungraceful" in data:
        import aws_sdk_arc_region_switch.types.ec2_ungraceful

        out["ungraceful"] = (
            aws_sdk_arc_region_switch.types.ec2_ungraceful.deserialize_aws_json_1_0(
                data["ungraceful"]
            )
        )
    if "targetPercent" in data:
        out["target_percent"] = data["targetPercent"]
    else:
        out["target_percent"] = 100
    if "capacityMonitoringApproach" in data:
        import aws_sdk_arc_region_switch.types.ec2_asg_capacity_monitoring_approach

        out["capacity_monitoring_approach"] = (
            aws_sdk_arc_region_switch.types.ec2_asg_capacity_monitoring_approach.deserialize_aws_json_1_0(
                data["capacityMonitoringApproach"]
            )
        )
    else:
        out["capacity_monitoring_approach"] = "sampledMaxInLast24Hours"
    return out
