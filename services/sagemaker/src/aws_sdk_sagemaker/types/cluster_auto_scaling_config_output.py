"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterAutoScalingConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sagemaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_auto_scaler_type
    import aws_sdk_sagemaker.types.cluster_auto_scaling_mode
    import aws_sdk_sagemaker.types.cluster_auto_scaling_status


class ClusterAutoScalingConfigOutput(TypedDict, closed=True):
    mode: "aws_sdk_sagemaker.types.cluster_auto_scaling_mode.ClusterAutoScalingMode"
    """<p>Describes whether autoscaling is enabled or disabled for the cluster.</p>"""
    auto_scaler_type: NotRequired[
        "aws_sdk_sagemaker.types.cluster_auto_scaler_type.ClusterAutoScalerType"
    ]
    """<p>The type of autoscaler configured for the cluster.</p>"""
    status: (
        "aws_sdk_sagemaker.types.cluster_auto_scaling_status.ClusterAutoScalingStatus"
    )
    """<p>The current status of the autoscaling configuration. Valid values are <code>InService</code>, <code>Failed</code>, <code>Creating</code>, and <code>Deleting</code>.</p>"""
    failure_message: NotRequired["str"]
    """<p>If the autoscaling status is <code>Failed</code>, this field contains a message describing the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterAutoScalingConfigOutput) -> dict:
    out: dict = {}
    import aws_sdk_sagemaker.types.cluster_auto_scaling_mode

    out["Mode"] = (
        aws_sdk_sagemaker.types.cluster_auto_scaling_mode.serialize_aws_json_1_1(
            value["mode"]
        )
    )
    if "auto_scaler_type" in value:
        import aws_sdk_sagemaker.types.cluster_auto_scaler_type

        out["AutoScalerType"] = (
            aws_sdk_sagemaker.types.cluster_auto_scaler_type.serialize_aws_json_1_1(
                value["auto_scaler_type"]
            )
        )
    import aws_sdk_sagemaker.types.cluster_auto_scaling_status

    out["Status"] = (
        aws_sdk_sagemaker.types.cluster_auto_scaling_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterAutoScalingConfigOutput:
    out: ClusterAutoScalingConfigOutput = {}  # type: ignore[typeddict-item]
    if "Mode" in data:
        import aws_sdk_sagemaker.types.cluster_auto_scaling_mode

        out["mode"] = (
            aws_sdk_sagemaker.types.cluster_auto_scaling_mode.deserialize_aws_json_1_1(
                data["Mode"]
            )
        )
    else:
        raise DeserializationError("ClusterAutoScalingConfigOutput.mode required")
    if "AutoScalerType" in data:
        import aws_sdk_sagemaker.types.cluster_auto_scaler_type

        out["auto_scaler_type"] = (
            aws_sdk_sagemaker.types.cluster_auto_scaler_type.deserialize_aws_json_1_1(
                data["AutoScalerType"]
            )
        )
    if "Status" in data:
        import aws_sdk_sagemaker.types.cluster_auto_scaling_status

        out["status"] = (
            aws_sdk_sagemaker.types.cluster_auto_scaling_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("ClusterAutoScalingConfigOutput.status required")
    if "FailureMessage" in data:
        out["failure_message"] = data["FailureMessage"]
    return out
