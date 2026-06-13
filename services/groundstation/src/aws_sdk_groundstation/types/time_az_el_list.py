"""Generated from Smithy shape ``com.amazonaws.groundstation#TimeAzElList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.time_az_el

TimeAzElList: TypeAlias = list["aws_sdk_groundstation.types.time_az_el.TimeAzEl"]


# --- restJson1 ser/de ---
def serialize_json(value: TimeAzElList) -> list:
    import aws_sdk_groundstation.types.time_az_el

    out: list = []
    for item in value:
        out.append(aws_sdk_groundstation.types.time_az_el.serialize_json(item))
    return out


def deserialize_json(data: list) -> TimeAzElList:
    import aws_sdk_groundstation.types.time_az_el

    out: TimeAzElList = []
    for item in data:
        out.append(aws_sdk_groundstation.types.time_az_el.deserialize_json(item))
    return out
