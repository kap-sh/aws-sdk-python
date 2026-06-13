"""Generated from Smithy shape ``com.amazonaws.grafana#WorkspaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_grafana.types.workspace_summary

WorkspaceList: TypeAlias = list[
    "aws_sdk_grafana.types.workspace_summary.WorkspaceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceList) -> list:
    import aws_sdk_grafana.types.workspace_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_grafana.types.workspace_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkspaceList:
    import aws_sdk_grafana.types.workspace_summary

    out: WorkspaceList = []
    for item in data:
        out.append(aws_sdk_grafana.types.workspace_summary.deserialize_json(item))
    return out
