"""Generated from Smithy shape ``com.amazonaws.arczonalshift#OutcomeAlarms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.control_condition

OutcomeAlarms: TypeAlias = list[
    "aws_sdk_arc_zonal_shift.types.control_condition.ControlCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: OutcomeAlarms) -> list:
    import aws_sdk_arc_zonal_shift.types.control_condition

    out: list = []
    for item in value:
        out.append(aws_sdk_arc_zonal_shift.types.control_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> OutcomeAlarms:
    import aws_sdk_arc_zonal_shift.types.control_condition

    out: OutcomeAlarms = []
    for item in data:
        out.append(
            aws_sdk_arc_zonal_shift.types.control_condition.deserialize_json(item)
        )
    return out
