"""Generated from Smithy shape ``com.amazonaws.iot#Percentiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.percent_pair

Percentiles: TypeAlias = list["aws_sdk_iot.types.percent_pair.PercentPair"]


# --- restJson1 ser/de ---
def serialize_json(value: Percentiles) -> list:
    import aws_sdk_iot.types.percent_pair

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.percent_pair.serialize_json(item))
    return out


def deserialize_json(data: list) -> Percentiles:
    import aws_sdk_iot.types.percent_pair

    out: Percentiles = []
    for item in data:
        out.append(aws_sdk_iot.types.percent_pair.deserialize_json(item))
    return out
