"""Generated from Smithy shape ``com.amazonaws.iot#CommandSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.command_summary

CommandSummaryList: TypeAlias = list["capo_iot.types.command_summary.CommandSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: CommandSummaryList) -> list:
    import capo_iot.types.command_summary

    out: list = []
    for item in value:
        out.append(capo_iot.types.command_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CommandSummaryList:
    import capo_iot.types.command_summary

    out: CommandSummaryList = []
    for item in data:
        out.append(capo_iot.types.command_summary.deserialize_json(item))
    return out
