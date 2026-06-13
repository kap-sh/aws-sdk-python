"""Generated from Smithy shape ``com.amazonaws.location#WiFiAccessPointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.wi_fi_access_point

WiFiAccessPointList: TypeAlias = list[
    "aws_sdk_location.types.wi_fi_access_point.WiFiAccessPoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: WiFiAccessPointList) -> list:
    import aws_sdk_location.types.wi_fi_access_point

    out: list = []
    for item in value:
        out.append(aws_sdk_location.types.wi_fi_access_point.serialize_json(item))
    return out


def deserialize_json(data: list) -> WiFiAccessPointList:
    import aws_sdk_location.types.wi_fi_access_point

    out: WiFiAccessPointList = []
    for item in data:
        out.append(aws_sdk_location.types.wi_fi_access_point.deserialize_json(item))
    return out
