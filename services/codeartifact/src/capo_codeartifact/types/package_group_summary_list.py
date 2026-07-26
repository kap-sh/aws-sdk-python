"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeartifact.types.package_group_summary

PackageGroupSummaryList: TypeAlias = list[
    "capo_codeartifact.types.package_group_summary.PackageGroupSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageGroupSummaryList) -> list:
    import capo_codeartifact.types.package_group_summary

    out: list = []
    for item in value:
        out.append(capo_codeartifact.types.package_group_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PackageGroupSummaryList:
    import capo_codeartifact.types.package_group_summary

    out: PackageGroupSummaryList = []
    for item in data:
        out.append(capo_codeartifact.types.package_group_summary.deserialize_json(item))
    return out
