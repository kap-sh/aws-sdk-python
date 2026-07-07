"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#AutoScaling``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__integer
    import aws_sdk_kafkaconnect.types.__integer_min1_max8
    import aws_sdk_kafkaconnect.types.scale_in_policy
    import aws_sdk_kafkaconnect.types.scale_out_policy


class AutoScaling(TypedDict, closed=True):
    max_worker_count: "aws_sdk_kafkaconnect.types.__integer.__integer"
    """<p>The maximum number of workers allocated to the connector.</p>"""
    mcu_count: "aws_sdk_kafkaconnect.types.__integer_min1_max8.__integerMin1Max8"
    """<p>The number of microcontroller units (MCUs) allocated to each connector worker. The valid values are 1,2,4,8.</p>"""
    min_worker_count: "aws_sdk_kafkaconnect.types.__integer.__integer"
    """<p>The minimum number of workers allocated to the connector.</p>"""
    scale_in_policy: NotRequired[
        "aws_sdk_kafkaconnect.types.scale_in_policy.ScaleInPolicy"
    ]
    """<p>The scale-in policy for the connector.</p>"""
    scale_out_policy: NotRequired[
        "aws_sdk_kafkaconnect.types.scale_out_policy.ScaleOutPolicy"
    ]
    """<p>The scale-out policy for the connector.</p>"""
    max_autoscaling_task_count: "aws_sdk_kafkaconnect.types.__integer.__integer"
    """<p>The maximum number of tasks allocated to the connector during autoscaling operations. Must be at least equal to maxWorkerCount.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoScaling) -> dict:
    out: dict = {}
    out["maxWorkerCount"] = value.get("max_worker_count", 0)
    out["mcuCount"] = value.get("mcu_count", 0)
    out["minWorkerCount"] = value.get("min_worker_count", 0)
    if "scale_in_policy" in value:
        import aws_sdk_kafkaconnect.types.scale_in_policy

        out["scaleInPolicy"] = (
            aws_sdk_kafkaconnect.types.scale_in_policy.serialize_json(
                value["scale_in_policy"]
            )
        )
    if "scale_out_policy" in value:
        import aws_sdk_kafkaconnect.types.scale_out_policy

        out["scaleOutPolicy"] = (
            aws_sdk_kafkaconnect.types.scale_out_policy.serialize_json(
                value["scale_out_policy"]
            )
        )
    out["maxAutoscalingTaskCount"] = value.get("max_autoscaling_task_count", 0)
    return out


def deserialize_json(data: dict) -> AutoScaling:
    out: AutoScaling = {}  # type: ignore[typeddict-item]
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
        import aws_sdk_kafkaconnect.types.scale_in_policy

        out["scale_in_policy"] = (
            aws_sdk_kafkaconnect.types.scale_in_policy.deserialize_json(
                data["scaleInPolicy"]
            )
        )
    if "scaleOutPolicy" in data:
        import aws_sdk_kafkaconnect.types.scale_out_policy

        out["scale_out_policy"] = (
            aws_sdk_kafkaconnect.types.scale_out_policy.deserialize_json(
                data["scaleOutPolicy"]
            )
        )
    if "maxAutoscalingTaskCount" in data:
        out["max_autoscaling_task_count"] = data["maxAutoscalingTaskCount"]
    else:
        out["max_autoscaling_task_count"] = 0
    return out
