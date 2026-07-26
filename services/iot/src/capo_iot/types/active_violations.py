"""Generated from Smithy shape ``com.amazonaws.iot#ActiveViolations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.active_violation

ActiveViolations: TypeAlias = list["capo_iot.types.active_violation.ActiveViolation"]


# --- restJson1 ser/de ---
def serialize_json(value: ActiveViolations) -> list:
    import capo_iot.types.active_violation

    out: list = []
    for item in value:
        out.append(capo_iot.types.active_violation.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActiveViolations:
    import capo_iot.types.active_violation

    out: ActiveViolations = []
    for item in data:
        out.append(capo_iot.types.active_violation.deserialize_json(item))
    return out
