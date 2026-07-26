"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeviceSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.device_summary

DeviceSummaries: TypeAlias = list["capo_sagemaker.types.device_summary.DeviceSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceSummaries) -> list:
    import capo_sagemaker.types.device_summary

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.device_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DeviceSummaries:
    import capo_sagemaker.types.device_summary

    out: DeviceSummaries = []
    for item in data:
        out.append(capo_sagemaker.types.device_summary.deserialize_aws_json_1_1(item))
    return out
