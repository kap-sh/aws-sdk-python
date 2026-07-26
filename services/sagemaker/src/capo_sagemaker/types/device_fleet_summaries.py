"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeviceFleetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.device_fleet_summary

DeviceFleetSummaries: TypeAlias = list[
    "capo_sagemaker.types.device_fleet_summary.DeviceFleetSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceFleetSummaries) -> list:
    import capo_sagemaker.types.device_fleet_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.device_fleet_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeviceFleetSummaries:
    import capo_sagemaker.types.device_fleet_summary

    out: DeviceFleetSummaries = []
    for item in data:
        out.append(
            capo_sagemaker.types.device_fleet_summary.deserialize_aws_json_1_1(item)
        )
    return out
