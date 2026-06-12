"""Generated from Smithy shape ``com.amazonaws.codebuild#Report``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.code_coverage_report_summary
    import aws_sdk_codebuild.types.non_empty_string
    import aws_sdk_codebuild.types.report_export_config
    import aws_sdk_codebuild.types.report_status_type
    import aws_sdk_codebuild.types.report_type
    import aws_sdk_codebuild.types.string
    import aws_sdk_codebuild.types.test_report_summary
    import aws_sdk_codebuild.types.timestamp
    import aws_sdk_codebuild.types.wrapper_boolean


class Report(TypedDict):
    arn: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p> The ARN of the report run. </p>"""
    type: NotRequired["aws_sdk_codebuild.types.report_type.ReportType"]
    """<p>The type of the report that was run.</p> <dl> <dt>CODE_COVERAGE</dt> <dd> <p>A code coverage report.</p> </dd> <dt>TEST</dt> <dd> <p>A test report.</p> </dd> </dl>"""
    name: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p> The name of the report that was run. </p>"""
    report_group_arn: NotRequired[
        "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ARN of the report group associated with this report. </p>"""
    execution_id: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p> The ARN of the build run that generated this report. </p>"""
    status: NotRequired["aws_sdk_codebuild.types.report_status_type.ReportStatusType"]
    """<p> The status of this report. </p>"""
    created: NotRequired["aws_sdk_codebuild.types.timestamp.Timestamp"]
    """<p> The date and time this report run occurred. </p>"""
    expired: NotRequired["aws_sdk_codebuild.types.timestamp.Timestamp"]
    """<p> The date and time a report expires. A report expires 30 days after it is created. An expired report is not available to view in CodeBuild. </p>"""
    export_config: NotRequired[
        "aws_sdk_codebuild.types.report_export_config.ReportExportConfig"
    ]
    """<p> Information about where the raw data used to generate this report was exported. </p>"""
    truncated: NotRequired["aws_sdk_codebuild.types.wrapper_boolean.WrapperBoolean"]
    """<p> A boolean that specifies if this report run is truncated. The list of test cases is truncated after the maximum number of test cases is reached. </p>"""
    test_summary: NotRequired[
        "aws_sdk_codebuild.types.test_report_summary.TestReportSummary"
    ]
    """<p> A <code>TestReportSummary</code> object that contains information about this test report. </p>"""
    code_coverage_summary: NotRequired[
        "aws_sdk_codebuild.types.code_coverage_report_summary.CodeCoverageReportSummary"
    ]
    """<p>A <code>CodeCoverageReportSummary</code> object that contains a code coverage summary for this report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Report) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "type" in value:
        import aws_sdk_codebuild.types.report_type

        out["type"] = aws_sdk_codebuild.types.report_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "report_group_arn" in value:
        out["reportGroupArn"] = value["report_group_arn"]
    if "execution_id" in value:
        out["executionId"] = value["execution_id"]
    if "status" in value:
        import aws_sdk_codebuild.types.report_status_type

        out["status"] = (
            aws_sdk_codebuild.types.report_status_type.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "created" in value:
        import aws_sdk_codebuild.types.timestamp

        out["created"] = aws_sdk_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["created"]
        )
    if "expired" in value:
        import aws_sdk_codebuild.types.timestamp

        out["expired"] = aws_sdk_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["expired"]
        )
    if "export_config" in value:
        import aws_sdk_codebuild.types.report_export_config

        out["exportConfig"] = (
            aws_sdk_codebuild.types.report_export_config.serialize_aws_json_1_1(
                value["export_config"]
            )
        )
    if "truncated" in value:
        out["truncated"] = value["truncated"]
    if "test_summary" in value:
        import aws_sdk_codebuild.types.test_report_summary

        out["testSummary"] = (
            aws_sdk_codebuild.types.test_report_summary.serialize_aws_json_1_1(
                value["test_summary"]
            )
        )
    if "code_coverage_summary" in value:
        import aws_sdk_codebuild.types.code_coverage_report_summary

        out["codeCoverageSummary"] = (
            aws_sdk_codebuild.types.code_coverage_report_summary.serialize_aws_json_1_1(
                value["code_coverage_summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Report:
    out: Report = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "type" in data:
        import aws_sdk_codebuild.types.report_type

        out["type"] = aws_sdk_codebuild.types.report_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if "name" in data:
        out["name"] = data["name"]
    if "reportGroupArn" in data:
        out["report_group_arn"] = data["reportGroupArn"]
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    if "status" in data:
        import aws_sdk_codebuild.types.report_status_type

        out["status"] = (
            aws_sdk_codebuild.types.report_status_type.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "created" in data:
        import aws_sdk_codebuild.types.timestamp

        out["created"] = aws_sdk_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["created"]
        )
    if "expired" in data:
        import aws_sdk_codebuild.types.timestamp

        out["expired"] = aws_sdk_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["expired"]
        )
    if "exportConfig" in data:
        import aws_sdk_codebuild.types.report_export_config

        out["export_config"] = (
            aws_sdk_codebuild.types.report_export_config.deserialize_aws_json_1_1(
                data["exportConfig"]
            )
        )
    if "truncated" in data:
        out["truncated"] = data["truncated"]
    if "testSummary" in data:
        import aws_sdk_codebuild.types.test_report_summary

        out["test_summary"] = (
            aws_sdk_codebuild.types.test_report_summary.deserialize_aws_json_1_1(
                data["testSummary"]
            )
        )
    if "codeCoverageSummary" in data:
        import aws_sdk_codebuild.types.code_coverage_report_summary

        out["code_coverage_summary"] = (
            aws_sdk_codebuild.types.code_coverage_report_summary.deserialize_aws_json_1_1(
                data["codeCoverageSummary"]
            )
        )
    return out
