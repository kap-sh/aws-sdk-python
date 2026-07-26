"""Generated from Smithy shape ``com.amazonaws.controlcatalog#Controls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controlcatalog.types.control_summary

Controls: TypeAlias = list["capo_controlcatalog.types.control_summary.ControlSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: Controls) -> list:
    import capo_controlcatalog.types.control_summary

    out: list = []
    for item in value:
        out.append(capo_controlcatalog.types.control_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> Controls:
    import capo_controlcatalog.types.control_summary

    out: Controls = []
    for item in data:
        out.append(capo_controlcatalog.types.control_summary.deserialize_json(item))
    return out
