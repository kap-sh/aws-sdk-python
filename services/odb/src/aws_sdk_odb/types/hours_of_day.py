"""Generated from Smithy shape ``com.amazonaws.odb#HoursOfDay``."""

from typing import TypeAlias

HoursOfDay: TypeAlias = list["int"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HoursOfDay) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> HoursOfDay:
    return list(data)
