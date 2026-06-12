"""Generated from Smithy shape ``com.amazonaws.connect#OperationalHours``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.operational_hour

OperationalHours: TypeAlias = list[
    "aws_sdk_connect.types.operational_hour.OperationalHour"
]


# --- restJson1 ser/de ---
def serialize_json(value: OperationalHours) -> list:
    import aws_sdk_connect.types.operational_hour

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.operational_hour.serialize_json(item))
    return out


def deserialize_json(data: list) -> OperationalHours:
    import aws_sdk_connect.types.operational_hour

    out: OperationalHours = []
    for item in data:
        out.append(aws_sdk_connect.types.operational_hour.deserialize_json(item))
    return out
