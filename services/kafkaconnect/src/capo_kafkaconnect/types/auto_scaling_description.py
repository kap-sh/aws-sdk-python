"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#AutoScalingDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__integer
    import capo_kafkaconnect.types.scale_in_policy_description
    import capo_kafkaconnect.types.scale_out_policy_description


class AutoScalingDescription(TypedDict, closed=True):
    max_worker_count: "capo_kafkaconnect.types.__integer.__integer"
    """<p>The maximum number of workers allocated to the connector.</p>"""
    mcu_count: "capo_kafkaconnect.types.__integer.__integer"
    """<p>The number of microcontroller units (MCUs) allocated to each connector worker. The valid values are 1,2,4,8.</p>"""
    min_worker_count: "capo_kafkaconnect.types.__integer.__integer"
    """<p>The minimum number of workers allocated to the connector.</p>"""
    scale_in_policy: NotRequired[
        "capo_kafkaconnect.types.scale_in_policy_description.ScaleInPolicyDescription"
    ]
    """<p>The scale-in policy for the connector.</p>"""
    scale_out_policy: NotRequired[
        "capo_kafkaconnect.types.scale_out_policy_description.ScaleOutPolicyDescription"
    ]
    """<p>The scale-out policy for the connector.</p>"""
    max_autoscaling_task_count: "capo_kafkaconnect.types.__integer.__integer"
    """<p>The maximum number of tasks allocated to the connector during autoscaling operations. Must be at least equal to maxWorkerCount.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoScalingDescription) -> dict:
    out: dict = {}
    out["maxWorkerCount"] = value.get("max_worker_count", 0)
    out["mcuCount"] = value.get("mcu_count", 0)
    out["minWorkerCount"] = value.get("min_worker_count", 0)
    if "scale_in_policy" in value:
        import capo_kafkaconnect.types.scale_in_policy_description

        out["scaleInPolicy"] = (
            capo_kafkaconnect.types.scale_in_policy_description.serialize_json(
                value["scale_in_policy"]
            )
        )
    if "scale_out_policy" in value:
        import capo_kafkaconnect.types.scale_out_policy_description

        out["scaleOutPolicy"] = (
            capo_kafkaconnect.types.scale_out_policy_description.serialize_json(
                value["scale_out_policy"]
            )
        )
    out["maxAutoscalingTaskCount"] = value.get("max_autoscaling_task_count", 0)
    return out


def deserialize_json(data: dict) -> AutoScalingDescription:
    out: AutoScalingDescription = {}  # type: ignore[typeddict-item]
    if "maxWorkerCount" in data:
        out["max_worker_count"] = data["maxWorkerCount"]
    else:
        out["max_worker_count"] = 0
    if "mcuCount" in data:
        out["mcu_count"] = data["mcuCount"]
    else:
        out["mcu_count"] = 0
    if "minWorkerCount" in data:
        out["min_worker_count"] = data["minWorkerCount"]
    else:
        out["min_worker_count"] = 0
    if "scaleInPolicy" in data:
        import capo_kafkaconnect.types.scale_in_policy_description

        out["scale_in_policy"] = (
            capo_kafkaconnect.types.scale_in_policy_description.deserialize_json(
                data["scaleInPolicy"]
            )
        )
    if "scaleOutPolicy" in data:
        import capo_kafkaconnect.types.scale_out_policy_description

        out["scale_out_policy"] = (
            capo_kafkaconnect.types.scale_out_policy_description.deserialize_json(
                data["scaleOutPolicy"]
            )
        )
    if "maxAutoscalingTaskCount" in data:
        out["max_autoscaling_task_count"] = data["maxAutoscalingTaskCount"]
    else:
        out["max_autoscaling_task_count"] = 0
    return out
