"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#EcsCapacityIncreaseConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.ecs_capacity_monitoring_approach
    import aws_sdk_arc_region_switch.types.ecs_ungraceful
    import aws_sdk_arc_region_switch.types.service_list


class EcsCapacityIncreaseConfiguration(TypedDict):
    timeout_minutes: "int"
    """<p>The timeout value specified for the configuration.</p>"""
    services: "aws_sdk_arc_region_switch.types.service_list.ServiceList"
    """<p>The services specified for the configuration.</p>"""
    ungraceful: NotRequired[
        "aws_sdk_arc_region_switch.types.ecs_ungraceful.EcsUngraceful"
    ]
    """<p>The settings for ungraceful execution.</p>"""
    target_percent: "int"
    """<p>The target percentage specified for the configuration. The default is 100.</p>"""
    capacity_monitoring_approach: "aws_sdk_arc_region_switch.types.ecs_capacity_monitoring_approach.EcsCapacityMonitoringApproach"
    """<p>The monitoring approach specified for the configuration, for example, <code>Most_Recent</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EcsCapacityIncreaseConfiguration) -> dict:
    out: dict = {}
    out["timeoutMinutes"] = value.get("timeout_minutes", 60)
    import aws_sdk_arc_region_switch.types.service_list

    out["services"] = (
        aws_sdk_arc_region_switch.types.service_list.serialize_aws_json_1_0(
            value["services"]
        )
    )
    if "ungraceful" in value:
        import aws_sdk_arc_region_switch.types.ecs_ungraceful

        out["ungraceful"] = (
            aws_sdk_arc_region_switch.types.ecs_ungraceful.serialize_aws_json_1_0(
                value["ungraceful"]
            )
        )
    out["targetPercent"] = value.get("target_percent", 100)
    import aws_sdk_arc_region_switch.types.ecs_capacity_monitoring_approach

    out["capacityMonitoringApproach"] = (
        aws_sdk_arc_region_switch.types.ecs_capacity_monitoring_approach.serialize_aws_json_1_0(
            value.get("capacity_monitoring_approach", "sampledMaxInLast24Hours")
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> EcsCapacityIncreaseConfiguration:
    out: EcsCapacityIncreaseConfiguration = {}  # type: ignore[typeddict-item]
    if "timeoutMinutes" in data:
        out["timeout_minutes"] = data["timeoutMinutes"]
    else:
        out["timeout_minutes"] = 60
    if "services" in data:
        import aws_sdk_arc_region_switch.types.service_list

        out["services"] = (
            aws_sdk_arc_region_switch.types.service_list.deserialize_aws_json_1_0(
                data["services"]
            )
        )
    else:
        raise DeserializationError("EcsCapacityIncreaseConfiguration.services required")
    if "ungraceful" in data:
        import aws_sdk_arc_region_switch.types.ecs_ungraceful

        out["ungraceful"] = (
            aws_sdk_arc_region_switch.types.ecs_ungraceful.deserialize_aws_json_1_0(
                data["ungraceful"]
            )
        )
    if "targetPercent" in data:
        out["target_percent"] = data["targetPercent"]
    else:
        out["target_percent"] = 100
    if "capacityMonitoringApproach" in data:
        import aws_sdk_arc_region_switch.types.ecs_capacity_monitoring_approach

        out["capacity_monitoring_approach"] = (
            aws_sdk_arc_region_switch.types.ecs_capacity_monitoring_approach.deserialize_aws_json_1_0(
                data["capacityMonitoringApproach"]
            )
        )
    else:
        out["capacity_monitoring_approach"] = "sampledMaxInLast24Hours"
    return out
