"""Generated from Smithy shape ``com.amazonaws.opensearch#PackageVersionHistoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.package_version_history

PackageVersionHistoryList: TypeAlias = list[
    "capo_opensearch.types.package_version_history.PackageVersionHistory"
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionHistoryList) -> list:
    import capo_opensearch.types.package_version_history

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.package_version_history.serialize_json(item))
    return out


def deserialize_json(data: list) -> PackageVersionHistoryList:
    import capo_opensearch.types.package_version_history

    out: PackageVersionHistoryList = []
    for item in data:
        out.append(capo_opensearch.types.package_version_history.deserialize_json(item))
    return out
