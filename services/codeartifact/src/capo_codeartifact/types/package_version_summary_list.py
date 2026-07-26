"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeartifact.types.package_version_summary

PackageVersionSummaryList: TypeAlias = list[
    "capo_codeartifact.types.package_version_summary.PackageVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionSummaryList) -> list:
    import capo_codeartifact.types.package_version_summary

    out: list = []
    for item in value:
        out.append(capo_codeartifact.types.package_version_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PackageVersionSummaryList:
    import capo_codeartifact.types.package_version_summary

    out: PackageVersionSummaryList = []
    for item in data:
        out.append(
            capo_codeartifact.types.package_version_summary.deserialize_json(item)
        )
    return out
