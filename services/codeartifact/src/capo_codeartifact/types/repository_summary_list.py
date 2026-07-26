"""Generated from Smithy shape ``com.amazonaws.codeartifact#RepositorySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeartifact.types.repository_summary

RepositorySummaryList: TypeAlias = list[
    "capo_codeartifact.types.repository_summary.RepositorySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RepositorySummaryList) -> list:
    import capo_codeartifact.types.repository_summary

    out: list = []
    for item in value:
        out.append(capo_codeartifact.types.repository_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> RepositorySummaryList:
    import capo_codeartifact.types.repository_summary

    out: RepositorySummaryList = []
    for item in data:
        out.append(capo_codeartifact.types.repository_summary.deserialize_json(item))
    return out
