"""Generated from Smithy shape ``com.amazonaws.iot#FleetMetricNameAndArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.fleet_metric_name_and_arn

FleetMetricNameAndArnList: TypeAlias = list[
    "capo_iot.types.fleet_metric_name_and_arn.FleetMetricNameAndArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: FleetMetricNameAndArnList) -> list:
    import capo_iot.types.fleet_metric_name_and_arn

    out: list = []
    for item in value:
        out.append(capo_iot.types.fleet_metric_name_and_arn.serialize_json(item))
    return out


def deserialize_json(data: list) -> FleetMetricNameAndArnList:
    import capo_iot.types.fleet_metric_name_and_arn

    out: FleetMetricNameAndArnList = []
    for item in data:
        out.append(capo_iot.types.fleet_metric_name_and_arn.deserialize_json(item))
    return out
