"""Generated from Smithy shape ``com.amazonaws.opensearch#PackageVersionHistoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.package_version_history

PackageVersionHistoryList: TypeAlias = list[
    "aws_sdk_opensearch.types.package_version_history.PackageVersionHistory"
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionHistoryList) -> list:
    import aws_sdk_opensearch.types.package_version_history

    out: list = []
    for item in value:
        out.append(
            aws_sdk_opensearch.types.package_version_history.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PackageVersionHistoryList:
    import aws_sdk_opensearch.types.package_version_history

    out: PackageVersionHistoryList = []
    for item in data:
        out.append(
            aws_sdk_opensearch.types.package_version_history.deserialize_json(item)
        )
    return out
