"""Generated from Smithy shape ``com.amazonaws.arczonalshift#BlockingAlarms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.control_condition

BlockingAlarms: TypeAlias = list[
    "aws_sdk_arc_zonal_shift.types.control_condition.ControlCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: BlockingAlarms) -> list:
    import aws_sdk_arc_zonal_shift.types.control_condition

    out: list = []
    for item in value:
        out.append(aws_sdk_arc_zonal_shift.types.control_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> BlockingAlarms:
    import aws_sdk_arc_zonal_shift.types.control_condition

    out: BlockingAlarms = []
    for item in data:
        out.append(
            aws_sdk_arc_zonal_shift.types.control_condition.deserialize_json(item)
        )
    return out
