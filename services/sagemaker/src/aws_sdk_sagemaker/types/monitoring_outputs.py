"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringOutputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_output

MonitoringOutputs: TypeAlias = list[
    "aws_sdk_sagemaker.types.monitoring_output.MonitoringOutput"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringOutputs) -> list:
    import aws_sdk_sagemaker.types.monitoring_output

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.monitoring_output.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MonitoringOutputs:
    import aws_sdk_sagemaker.types.monitoring_output

    out: MonitoringOutputs = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.monitoring_output.deserialize_aws_json_1_1(item)
        )
    return out
