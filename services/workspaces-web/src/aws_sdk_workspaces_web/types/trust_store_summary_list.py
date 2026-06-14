"""Generated from Smithy shape ``com.amazonaws.workspacesweb#TrustStoreSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.trust_store_summary

TrustStoreSummaryList: TypeAlias = list[
    "aws_sdk_workspaces_web.types.trust_store_summary.TrustStoreSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TrustStoreSummaryList) -> list:
    import aws_sdk_workspaces_web.types.trust_store_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces_web.types.trust_store_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TrustStoreSummaryList:
    import aws_sdk_workspaces_web.types.trust_store_summary

    out: TrustStoreSummaryList = []
    for item in data:
        out.append(
            aws_sdk_workspaces_web.types.trust_store_summary.deserialize_json(item)
        )
    return out
