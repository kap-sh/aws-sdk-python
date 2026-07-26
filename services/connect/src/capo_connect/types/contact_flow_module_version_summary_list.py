"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowModuleVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_module_version_summary

ContactFlowModuleVersionSummaryList: TypeAlias = list[
    "capo_connect.types.contact_flow_module_version_summary.ContactFlowModuleVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowModuleVersionSummaryList) -> list:
    import capo_connect.types.contact_flow_module_version_summary

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.contact_flow_module_version_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ContactFlowModuleVersionSummaryList:
    import capo_connect.types.contact_flow_module_version_summary

    out: ContactFlowModuleVersionSummaryList = []
    for item in data:
        out.append(
            capo_connect.types.contact_flow_module_version_summary.deserialize_json(
                item
            )
        )
    return out
