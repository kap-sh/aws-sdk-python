"""Generated from Smithy shape ``com.amazonaws.licensemanager#ReportGenerator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.report_context
    import capo_license_manager.types.report_frequency
    import capo_license_manager.types.report_type_list
    import capo_license_manager.types.s3_location
    import capo_license_manager.types.string
    import capo_license_manager.types.tag_list


class ReportGenerator(TypedDict, closed=True):
    report_generator_name: NotRequired["capo_license_manager.types.string.String"]
    """<p>Name of the report generator.</p>"""
    report_type: NotRequired[
        "capo_license_manager.types.report_type_list.ReportTypeList"
    ]
    """<p>Type of reports that are generated.</p>"""
    report_context: NotRequired[
        "capo_license_manager.types.report_context.ReportContext"
    ]
    """<p>License configuration type for this generator.</p>"""
    report_frequency: NotRequired[
        "capo_license_manager.types.report_frequency.ReportFrequency"
    ]
    """<p>Details about how frequently reports are generated.</p>"""
    license_manager_report_generator_arn: NotRequired[
        "capo_license_manager.types.string.String"
    ]
    """<p>Amazon Resource Name (ARN) of the report generator.</p>"""
    last_run_status: NotRequired["capo_license_manager.types.string.String"]
    """<p>Status of the last report generation attempt.</p>"""
    last_run_failure_reason: NotRequired["capo_license_manager.types.string.String"]
    """<p>Failure message for the last report generation attempt.</p>"""
    last_report_generation_time: NotRequired["capo_license_manager.types.string.String"]
    """<p>Time the last report was generated at.</p>"""
    report_creator_account: NotRequired["capo_license_manager.types.string.String"]
    """<p>The Amazon Web Services account ID used to create the report generator.</p>"""
    description: NotRequired["capo_license_manager.types.string.String"]
    """<p>Description of the report generator.</p>"""
    s3_location: NotRequired["capo_license_manager.types.s3_location.S3Location"]
    """<p>Details of the S3 bucket that report generator reports are published to.</p>"""
    create_time: NotRequired["capo_license_manager.types.string.String"]
    """<p>Time the report was created.</p>"""
    tags: NotRequired["capo_license_manager.types.tag_list.TagList"]
    """<p>Tags associated with the report generator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportGenerator) -> dict:
    out: dict = {}
    if "report_generator_name" in value:
        out["ReportGeneratorName"] = value["report_generator_name"]
    if "report_type" in value:
        import capo_license_manager.types.report_type_list

        out["ReportType"] = (
            capo_license_manager.types.report_type_list.serialize_aws_json_1_1(
                value["report_type"]
            )
        )
    if "report_context" in value:
        import capo_license_manager.types.report_context

        out["ReportContext"] = (
            capo_license_manager.types.report_context.serialize_aws_json_1_1(
                value["report_context"]
            )
        )
    if "report_frequency" in value:
        import capo_license_manager.types.report_frequency

        out["ReportFrequency"] = (
            capo_license_manager.types.report_frequency.serialize_aws_json_1_1(
                value["report_frequency"]
            )
        )
    if "license_manager_report_generator_arn" in value:
        out["LicenseManagerReportGeneratorArn"] = value[
            "license_manager_report_generator_arn"
        ]
    if "last_run_status" in value:
        out["LastRunStatus"] = value["last_run_status"]
    if "last_run_failure_reason" in value:
        out["LastRunFailureReason"] = value["last_run_failure_reason"]
    if "last_report_generation_time" in value:
        out["LastReportGenerationTime"] = value["last_report_generation_time"]
    if "report_creator_account" in value:
        out["ReportCreatorAccount"] = value["report_creator_account"]
    if "description" in value:
        out["Description"] = value["description"]
    if "s3_location" in value:
        import capo_license_manager.types.s3_location

        out["S3Location"] = (
            capo_license_manager.types.s3_location.serialize_aws_json_1_1(
                value["s3_location"]
            )
        )
    if "create_time" in value:
        out["CreateTime"] = value["create_time"]
    if "tags" in value:
        import capo_license_manager.types.tag_list

        out["Tags"] = capo_license_manager.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportGenerator:
    out: ReportGenerator = {}  # type: ignore[typeddict-item]
    if "ReportGeneratorName" in data:
        out["report_generator_name"] = data["ReportGeneratorName"]
    if "ReportType" in data:
        import capo_license_manager.types.report_type_list

        out["report_type"] = (
            capo_license_manager.types.report_type_list.deserialize_aws_json_1_1(
                data["ReportType"]
            )
        )
    if "ReportContext" in data:
        import capo_license_manager.types.report_context

        out["report_context"] = (
            capo_license_manager.types.report_context.deserialize_aws_json_1_1(
                data["ReportContext"]
            )
        )
    if "ReportFrequency" in data:
        import capo_license_manager.types.report_frequency

        out["report_frequency"] = (
            capo_license_manager.types.report_frequency.deserialize_aws_json_1_1(
                data["ReportFrequency"]
            )
        )
    if "LicenseManagerReportGeneratorArn" in data:
        out["license_manager_report_generator_arn"] = data[
            "LicenseManagerReportGeneratorArn"
        ]
    if "LastRunStatus" in data:
        out["last_run_status"] = data["LastRunStatus"]
    if "LastRunFailureReason" in data:
        out["last_run_failure_reason"] = data["LastRunFailureReason"]
    if "LastReportGenerationTime" in data:
        out["last_report_generation_time"] = data["LastReportGenerationTime"]
    if "ReportCreatorAccount" in data:
        out["report_creator_account"] = data["ReportCreatorAccount"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "S3Location" in data:
        import capo_license_manager.types.s3_location

        out["s3_location"] = (
            capo_license_manager.types.s3_location.deserialize_aws_json_1_1(
                data["S3Location"]
            )
        )
    if "CreateTime" in data:
        out["create_time"] = data["CreateTime"]
    if "Tags" in data:
        import capo_license_manager.types.tag_list

        out["tags"] = capo_license_manager.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
