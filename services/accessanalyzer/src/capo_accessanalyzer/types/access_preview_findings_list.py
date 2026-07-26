"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AccessPreviewFindingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.access_preview_finding

AccessPreviewFindingsList: TypeAlias = list[
    "capo_accessanalyzer.types.access_preview_finding.AccessPreviewFinding"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessPreviewFindingsList) -> list:
    import capo_accessanalyzer.types.access_preview_finding

    out: list = []
    for item in value:
        out.append(
            capo_accessanalyzer.types.access_preview_finding.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AccessPreviewFindingsList:
    import capo_accessanalyzer.types.access_preview_finding

    out: AccessPreviewFindingsList = []
    for item in data:
        out.append(
            capo_accessanalyzer.types.access_preview_finding.deserialize_json(item)
        )
    return out
