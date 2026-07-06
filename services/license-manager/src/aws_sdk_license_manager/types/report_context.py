"""Generated from Smithy shape ``com.amazonaws.licensemanager#ReportContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.arn_list
    import aws_sdk_license_manager.types.date_time


class ReportContext(TypedDict, closed=True):
    license_configuration_arns: "aws_sdk_license_manager.types.arn_list.ArnList"
    """<p>Amazon Resource Name (ARN) of the license configuration that this generator reports on.</p>"""
    license_asset_group_arns: NotRequired[
        "aws_sdk_license_manager.types.arn_list.ArnList"
    ]
    """<p>Amazon Resource Names (ARNs) of the license asset groups to include in the report.</p>"""
    report_start_date: NotRequired["aws_sdk_license_manager.types.date_time.DateTime"]
    """<p>Start date for the report data collection period.</p>"""
    report_end_date: NotRequired["aws_sdk_license_manager.types.date_time.DateTime"]
    """<p>End date for the report data collection period.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportContext) -> dict:
    out: dict = {}
    import aws_sdk_license_manager.types.arn_list

    out["licenseConfigurationArns"] = (
        aws_sdk_license_manager.types.arn_list.serialize_aws_json_1_1(
            value.get("license_configuration_arns", [])
        )
    )
    if "license_asset_group_arns" in value:
        import aws_sdk_license_manager.types.arn_list

        out["licenseAssetGroupArns"] = (
            aws_sdk_license_manager.types.arn_list.serialize_aws_json_1_1(
                value["license_asset_group_arns"]
            )
        )
    if "report_start_date" in value:
        import aws_sdk_license_manager.types.date_time

        out["reportStartDate"] = (
            aws_sdk_license_manager.types.date_time.serialize_aws_json_1_1(
                value["report_start_date"]
            )
        )
    if "report_end_date" in value:
        import aws_sdk_license_manager.types.date_time

        out["reportEndDate"] = (
            aws_sdk_license_manager.types.date_time.serialize_aws_json_1_1(
                value["report_end_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportContext:
    out: ReportContext = {}  # type: ignore[typeddict-item]
    if "licenseConfigurationArns" in data:
        import aws_sdk_license_manager.types.arn_list

        out["license_configuration_arns"] = (
            aws_sdk_license_manager.types.arn_list.deserialize_aws_json_1_1(
                data["licenseConfigurationArns"]
            )
        )
    else:
        out["license_configuration_arns"] = []
    if "licenseAssetGroupArns" in data:
        import aws_sdk_license_manager.types.arn_list

        out["license_asset_group_arns"] = (
            aws_sdk_license_manager.types.arn_list.deserialize_aws_json_1_1(
                data["licenseAssetGroupArns"]
            )
        )
    if "reportStartDate" in data:
        import aws_sdk_license_manager.types.date_time

        out["report_start_date"] = (
            aws_sdk_license_manager.types.date_time.deserialize_aws_json_1_1(
                data["reportStartDate"]
            )
        )
    if "reportEndDate" in data:
        import aws_sdk_license_manager.types.date_time

        out["report_end_date"] = (
            aws_sdk_license_manager.types.date_time.deserialize_aws_json_1_1(
                data["reportEndDate"]
            )
        )
    return out
