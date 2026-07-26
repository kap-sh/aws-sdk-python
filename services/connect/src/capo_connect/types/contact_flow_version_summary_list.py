"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_version_summary

ContactFlowVersionSummaryList: TypeAlias = list[
    "capo_connect.types.contact_flow_version_summary.ContactFlowVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowVersionSummaryList) -> list:
    import capo_connect.types.contact_flow_version_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.contact_flow_version_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContactFlowVersionSummaryList:
    import capo_connect.types.contact_flow_version_summary

    out: ContactFlowVersionSummaryList = []
    for item in data:
        out.append(
            capo_connect.types.contact_flow_version_summary.deserialize_json(item)
        )
    return out
