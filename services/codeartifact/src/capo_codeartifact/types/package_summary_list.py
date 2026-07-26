"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeartifact.types.package_summary

PackageSummaryList: TypeAlias = list[
    "capo_codeartifact.types.package_summary.PackageSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageSummaryList) -> list:
    import capo_codeartifact.types.package_summary

    out: list = []
    for item in value:
        out.append(capo_codeartifact.types.package_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PackageSummaryList:
    import capo_codeartifact.types.package_summary

    out: PackageSummaryList = []
    for item in data:
        out.append(capo_codeartifact.types.package_summary.deserialize_json(item))
    return out
