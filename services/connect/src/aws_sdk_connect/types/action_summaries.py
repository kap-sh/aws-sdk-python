"""Generated from Smithy shape ``com.amazonaws.connect#ActionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.action_summary

ActionSummaries: TypeAlias = list["aws_sdk_connect.types.action_summary.ActionSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ActionSummaries) -> list:
    import aws_sdk_connect.types.action_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.action_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActionSummaries:
    import aws_sdk_connect.types.action_summary

    out: ActionSummaries = []
    for item in data:
        out.append(aws_sdk_connect.types.action_summary.deserialize_json(item))
    return out
