"""Generated from Smithy shape ``com.amazonaws.qbusiness#Actions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.action_summary

Actions: TypeAlias = list["capo_qbusiness.types.action_summary.ActionSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: Actions) -> list:
    import capo_qbusiness.types.action_summary

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.action_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> Actions:
    import capo_qbusiness.types.action_summary

    out: Actions = []
    for item in data:
        out.append(capo_qbusiness.types.action_summary.deserialize_json(item))
    return out
