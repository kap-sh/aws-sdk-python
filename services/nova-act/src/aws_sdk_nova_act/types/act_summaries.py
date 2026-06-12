"""Generated from Smithy shape ``com.amazonaws.novaact#ActSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.act_summary

ActSummaries: TypeAlias = list["aws_sdk_nova_act.types.act_summary.ActSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ActSummaries) -> list:
    import aws_sdk_nova_act.types.act_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_nova_act.types.act_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActSummaries:
    import aws_sdk_nova_act.types.act_summary

    out: ActSummaries = []
    for item in data:
        out.append(aws_sdk_nova_act.types.act_summary.deserialize_json(item))
    return out
