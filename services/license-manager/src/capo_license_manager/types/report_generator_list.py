"""Generated from Smithy shape ``com.amazonaws.licensemanager#ReportGeneratorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager.types.report_generator

ReportGeneratorList: TypeAlias = list[
    "capo_license_manager.types.report_generator.ReportGenerator"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportGeneratorList) -> list:
    import capo_license_manager.types.report_generator

    out: list = []
    for item in value:
        out.append(
            capo_license_manager.types.report_generator.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReportGeneratorList:
    import capo_license_manager.types.report_generator

    out: ReportGeneratorList = []
    for item in data:
        out.append(
            capo_license_manager.types.report_generator.deserialize_aws_json_1_1(item)
        )
    return out
