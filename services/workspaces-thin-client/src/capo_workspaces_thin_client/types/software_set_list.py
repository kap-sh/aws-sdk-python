"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#SoftwareSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.software_set_summary

SoftwareSetList: TypeAlias = list[
    "capo_workspaces_thin_client.types.software_set_summary.SoftwareSetSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareSetList) -> list:
    import capo_workspaces_thin_client.types.software_set_summary

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_thin_client.types.software_set_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SoftwareSetList:
    import capo_workspaces_thin_client.types.software_set_summary

    out: SoftwareSetList = []
    for item in data:
        out.append(
            capo_workspaces_thin_client.types.software_set_summary.deserialize_json(
                item
            )
        )
    return out
