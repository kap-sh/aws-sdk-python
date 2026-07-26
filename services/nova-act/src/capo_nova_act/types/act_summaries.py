"""Generated from Smithy shape ``com.amazonaws.novaact#ActSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_nova_act.types.act_summary

ActSummaries: TypeAlias = list["capo_nova_act.types.act_summary.ActSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ActSummaries) -> list:
    import capo_nova_act.types.act_summary

    out: list = []
    for item in value:
        out.append(capo_nova_act.types.act_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActSummaries:
    import capo_nova_act.types.act_summary

    out: ActSummaries = []
    for item in data:
        out.append(capo_nova_act.types.act_summary.deserialize_json(item))
    return out
