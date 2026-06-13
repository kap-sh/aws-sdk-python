"""Generated from Smithy shape ``com.amazonaws.amp#WorkspaceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amp.types.workspace_summary

WorkspaceSummaryList: TypeAlias = list[
    "aws_sdk_amp.types.workspace_summary.WorkspaceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceSummaryList) -> list:
    import aws_sdk_amp.types.workspace_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_amp.types.workspace_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkspaceSummaryList:
    import aws_sdk_amp.types.workspace_summary

    out: WorkspaceSummaryList = []
    for item in data:
        out.append(aws_sdk_amp.types.workspace_summary.deserialize_json(item))
    return out
