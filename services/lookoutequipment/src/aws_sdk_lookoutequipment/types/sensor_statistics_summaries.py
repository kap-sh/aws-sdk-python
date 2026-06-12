"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#SensorStatisticsSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.sensor_statistics_summary

SensorStatisticsSummaries: TypeAlias = list[
    "aws_sdk_lookoutequipment.types.sensor_statistics_summary.SensorStatisticsSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SensorStatisticsSummaries) -> list:
    import aws_sdk_lookoutequipment.types.sensor_statistics_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lookoutequipment.types.sensor_statistics_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SensorStatisticsSummaries:
    import aws_sdk_lookoutequipment.types.sensor_statistics_summary

    out: SensorStatisticsSummaries = []
    for item in data:
        out.append(
            aws_sdk_lookoutequipment.types.sensor_statistics_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
