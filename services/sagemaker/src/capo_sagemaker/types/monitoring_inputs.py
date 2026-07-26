"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringInputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.monitoring_input

MonitoringInputs: TypeAlias = list[
    "capo_sagemaker.types.monitoring_input.MonitoringInput"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringInputs) -> list:
    import capo_sagemaker.types.monitoring_input

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.monitoring_input.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MonitoringInputs:
    import capo_sagemaker.types.monitoring_input

    out: MonitoringInputs = []
    for item in data:
        out.append(capo_sagemaker.types.monitoring_input.deserialize_aws_json_1_1(item))
    return out
