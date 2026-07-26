"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#SensorStatisticsSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lookoutequipment.types.sensor_statistics_summary

SensorStatisticsSummaries: TypeAlias = list[
    "capo_lookoutequipment.types.sensor_statistics_summary.SensorStatisticsSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SensorStatisticsSummaries) -> list:
    import capo_lookoutequipment.types.sensor_statistics_summary

    out: list = []
    for item in value:
        out.append(
            capo_lookoutequipment.types.sensor_statistics_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SensorStatisticsSummaries:
    import capo_lookoutequipment.types.sensor_statistics_summary

    out: SensorStatisticsSummaries = []
    for item in data:
        out.append(
            capo_lookoutequipment.types.sensor_statistics_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
