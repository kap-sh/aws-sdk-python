"""Generated from Smithy shape ``com.amazonaws.workspacesweb#PortalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.portal_summary

PortalList: TypeAlias = list[
    "aws_sdk_workspaces_web.types.portal_summary.PortalSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PortalList) -> list:
    import aws_sdk_workspaces_web.types.portal_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_workspaces_web.types.portal_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PortalList:
    import aws_sdk_workspaces_web.types.portal_summary

    out: PortalList = []
    for item in data:
        out.append(aws_sdk_workspaces_web.types.portal_summary.deserialize_json(item))
    return out
