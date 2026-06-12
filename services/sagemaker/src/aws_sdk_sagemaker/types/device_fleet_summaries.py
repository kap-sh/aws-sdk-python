"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeviceFleetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.device_fleet_summary

DeviceFleetSummaries: TypeAlias = list[
    "aws_sdk_sagemaker.types.device_fleet_summary.DeviceFleetSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceFleetSummaries) -> list:
    import aws_sdk_sagemaker.types.device_fleet_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.device_fleet_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeviceFleetSummaries:
    import aws_sdk_sagemaker.types.device_fleet_summary

    out: DeviceFleetSummaries = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.device_fleet_summary.deserialize_aws_json_1_1(item)
        )
    return out
