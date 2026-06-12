"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.package_group_summary

PackageGroupSummaryList: TypeAlias = list[
    "aws_sdk_codeartifact.types.package_group_summary.PackageGroupSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageGroupSummaryList) -> list:
    import aws_sdk_codeartifact.types.package_group_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codeartifact.types.package_group_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PackageGroupSummaryList:
    import aws_sdk_codeartifact.types.package_group_summary

    out: PackageGroupSummaryList = []
    for item in data:
        out.append(
            aws_sdk_codeartifact.types.package_group_summary.deserialize_json(item)
        )
    return out
