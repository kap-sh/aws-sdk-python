"""Generated from Smithy shape ``com.amazonaws.emr#SimpleScalingPolicyConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.adjustment_type
    import aws_sdk_emr.types.integer


class SimpleScalingPolicyConfiguration(TypedDict):
    adjustment_type: NotRequired["aws_sdk_emr.types.adjustment_type.AdjustmentType"]
    """<p>The way in which Amazon EC2 instances are added (if <code>ScalingAdjustment</code> is a positive number) or terminated (if <code>ScalingAdjustment</code> is a negative number) each time the scaling activity is triggered. <code>CHANGE_IN_CAPACITY</code> is the default. <code>CHANGE_IN_CAPACITY</code> indicates that the Amazon EC2 instance count increments or decrements by <code>ScalingAdjustment</code>, which should be expressed as an integer. <code>PERCENT_CHANGE_IN_CAPACITY</code> indicates the instance count increments or decrements by the percentage specified by <code>ScalingAdjustment</code>, which should be expressed as an integer. For example, 20 indicates an increase in 20% increments of cluster capacity. <code>EXACT_CAPACITY</code> indicates the scaling activity results in an instance group with the number of Amazon EC2 instances specified by <code>ScalingAdjustment</code>, which should be expressed as a positive integer.</p>"""
    scaling_adjustment: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p>The amount by which to scale in or scale out, based on the specified <code>AdjustmentType</code>. A positive value adds to the instance group's Amazon EC2 instance count while a negative number removes instances. If <code>AdjustmentType</code> is set to <code>EXACT_CAPACITY</code>, the number should only be a positive integer. If <code>AdjustmentType</code> is set to <code>PERCENT_CHANGE_IN_CAPACITY</code>, the value should express the percentage as an integer. For example, -20 indicates a decrease in 20% increments of cluster capacity.</p>"""
    cool_down: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p>The amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities can start. The default value is 0.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SimpleScalingPolicyConfiguration) -> dict:
    out: dict = {}
    if "adjustment_type" in value:
        import aws_sdk_emr.types.adjustment_type

        out["AdjustmentType"] = (
            aws_sdk_emr.types.adjustment_type.serialize_aws_json_1_1(
                value["adjustment_type"]
            )
        )
    if "scaling_adjustment" in value:
        out["ScalingAdjustment"] = value["scaling_adjustment"]
    if "cool_down" in value:
        out["CoolDown"] = value["cool_down"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SimpleScalingPolicyConfiguration:
    out: SimpleScalingPolicyConfiguration = {}  # type: ignore[typeddict-item]
    if "AdjustmentType" in data:
        import aws_sdk_emr.types.adjustment_type

        out["adjustment_type"] = (
            aws_sdk_emr.types.adjustment_type.deserialize_aws_json_1_1(
                data["AdjustmentType"]
            )
        )
    if "ScalingAdjustment" in data:
        out["scaling_adjustment"] = data["ScalingAdjustment"]
    if "CoolDown" in data:
        out["cool_down"] = data["CoolDown"]
    return out
