"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#AutoScalingUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kafkaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__integer
    import aws_sdk_kafkaconnect.types.__integer_min1_max8
    import aws_sdk_kafkaconnect.types.scale_in_policy_update
    import aws_sdk_kafkaconnect.types.scale_out_policy_update


class AutoScalingUpdate(TypedDict, closed=True):
    max_worker_count: "aws_sdk_kafkaconnect.types.__integer.__integer"
    """<p>The target maximum number of workers allocated to the connector.</p>"""
    mcu_count: "aws_sdk_kafkaconnect.types.__integer_min1_max8.__integerMin1Max8"
    """<p>The target number of microcontroller units (MCUs) allocated to each connector worker. The valid values are 1,2,4,8.</p>"""
    min_worker_count: "aws_sdk_kafkaconnect.types.__integer.__integer"
    """<p>The target minimum number of workers allocated to the connector.</p>"""
    scale_in_policy: (
        "aws_sdk_kafkaconnect.types.scale_in_policy_update.ScaleInPolicyUpdate"
    )
    """<p>The target scale-in policy for the connector.</p>"""
    scale_out_policy: (
        "aws_sdk_kafkaconnect.types.scale_out_policy_update.ScaleOutPolicyUpdate"
    )
    """<p>The target scale-out policy for the connector.</p>"""
    max_autoscaling_task_count: "aws_sdk_kafkaconnect.types.__integer.__integer"
    """<p>The maximum number of tasks allocated to the connector during autoscaling operations. Must be at least equal to maxWorkerCount.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoScalingUpdate) -> dict:
    out: dict = {}
    out["maxWorkerCount"] = value.get("max_worker_count", 0)
    out["mcuCount"] = value.get("mcu_count", 0)
    out["minWorkerCount"] = value.get("min_worker_count", 0)
    import aws_sdk_kafkaconnect.types.scale_in_policy_update

    out["scaleInPolicy"] = (
        aws_sdk_kafkaconnect.types.scale_in_policy_update.serialize_json(
            value["scale_in_policy"]
        )
    )
    import aws_sdk_kafkaconnect.types.scale_out_policy_update

    out["scaleOutPolicy"] = (
        aws_sdk_kafkaconnect.types.scale_out_policy_update.serialize_json(
            value["scale_out_policy"]
        )
    )
    out["maxAutoscalingTaskCount"] = value.get("max_autoscaling_task_count", 0)
    return out


def deserialize_json(data: dict) -> AutoScalingUpdate:
    out: AutoScalingUpdate = {}  # type: ignore[typeddict-item]
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
        import aws_sdk_kafkaconnect.types.scale_in_policy_update

        out["scale_in_policy"] = (
            aws_sdk_kafkaconnect.types.scale_in_policy_update.deserialize_json(
                data["scaleInPolicy"]
            )
        )
    else:
        raise DeserializationError("AutoScalingUpdate.scale_in_policy required")
    if "scaleOutPolicy" in data:
        import aws_sdk_kafkaconnect.types.scale_out_policy_update

        out["scale_out_policy"] = (
            aws_sdk_kafkaconnect.types.scale_out_policy_update.deserialize_json(
                data["scaleOutPolicy"]
            )
        )
    else:
        raise DeserializationError("AutoScalingUpdate.scale_out_policy required")
    if "maxAutoscalingTaskCount" in data:
        out["max_autoscaling_task_count"] = data["maxAutoscalingTaskCount"]
    else:
        out["max_autoscaling_task_count"] = 0
    return out
