"""Generated from Smithy shape ``com.amazonaws.iot#PackageSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.package_summary

PackageSummaryList: TypeAlias = list["aws_sdk_iot.types.package_summary.PackageSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: PackageSummaryList) -> list:
    import aws_sdk_iot.types.package_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.package_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PackageSummaryList:
    import aws_sdk_iot.types.package_summary

    out: PackageSummaryList = []
    for item in data:
        out.append(aws_sdk_iot.types.package_summary.deserialize_json(item))
    return out
