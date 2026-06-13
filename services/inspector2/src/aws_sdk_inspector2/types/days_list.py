"""Generated from Smithy shape ``com.amazonaws.inspector2#DaysList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.day

DaysList: TypeAlias = list["aws_sdk_inspector2.types.day.Day"]


# --- restJson1 ser/de ---
def serialize_json(value: DaysList) -> list:
    import aws_sdk_inspector2.types.day

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.day.serialize_json(item))
    return out


def deserialize_json(data: list) -> DaysList:
    import aws_sdk_inspector2.types.day

    out: DaysList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.day.deserialize_json(item))
    return out
