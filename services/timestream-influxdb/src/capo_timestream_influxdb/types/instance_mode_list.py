"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#InstanceModeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.instance_mode

InstanceModeList: TypeAlias = list[
    "capo_timestream_influxdb.types.instance_mode.InstanceMode"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceModeList) -> list:
    import capo_timestream_influxdb.types.instance_mode

    out: list = []
    for item in value:
        out.append(
            capo_timestream_influxdb.types.instance_mode.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InstanceModeList:
    import capo_timestream_influxdb.types.instance_mode

    out: InstanceModeList = []
    for item in data:
        out.append(
            capo_timestream_influxdb.types.instance_mode.deserialize_aws_json_1_0(item)
        )
    return out
