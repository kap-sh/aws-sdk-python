"""Generated from Smithy shape ``com.amazonaws.licensemanager#ReportTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.report_type

ReportTypeList: TypeAlias = list["aws_sdk_license_manager.types.report_type.ReportType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportTypeList) -> list:
    import aws_sdk_license_manager.types.report_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_license_manager.types.report_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReportTypeList:
    import aws_sdk_license_manager.types.report_type

    out: ReportTypeList = []
    for item in data:
        out.append(
            aws_sdk_license_manager.types.report_type.deserialize_aws_json_1_1(item)
        )
    return out
