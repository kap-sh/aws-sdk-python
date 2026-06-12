"""Generated from Smithy shape ``com.amazonaws.iot#PackageVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.package_version_summary

PackageVersionSummaryList: TypeAlias = list[
    "aws_sdk_iot.types.package_version_summary.PackageVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionSummaryList) -> list:
    import aws_sdk_iot.types.package_version_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.package_version_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PackageVersionSummaryList:
    import aws_sdk_iot.types.package_version_summary

    out: PackageVersionSummaryList = []
    for item in data:
        out.append(aws_sdk_iot.types.package_version_summary.deserialize_json(item))
    return out
