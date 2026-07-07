"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeTestSetDiscrepancyReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.failure_reasons
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.presigned_s3_url
    import aws_sdk_lex_models_v2.types.test_set_discrepancy_errors
    import aws_sdk_lex_models_v2.types.test_set_discrepancy_report_resource_target
    import aws_sdk_lex_models_v2.types.test_set_discrepancy_report_status
    import aws_sdk_lex_models_v2.types.timestamp


class DescribeTestSetDiscrepancyReportResponse(TypedDict, closed=True):
    test_set_discrepancy_report_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the test set discrepancy report to describe.</p>"""
    test_set_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The test set Id for the test set discrepancy report.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The time and date of creation for the test set discrepancy report.</p>"""
    target: NotRequired[
        "aws_sdk_lex_models_v2.types.test_set_discrepancy_report_resource_target.TestSetDiscrepancyReportResourceTarget"
    ]
    """<p>The target bot location for the test set discrepancy report.</p>"""
    test_set_discrepancy_report_status: NotRequired[
        "aws_sdk_lex_models_v2.types.test_set_discrepancy_report_status.TestSetDiscrepancyReportStatus"
    ]
    """<p>The status for the test set discrepancy report.</p>"""
    last_updated_data_time: NotRequired[
        "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>The date and time of the last update for the test set discrepancy report.</p>"""
    test_set_discrepancy_top_errors: NotRequired[
        "aws_sdk_lex_models_v2.types.test_set_discrepancy_errors.TestSetDiscrepancyErrors"
    ]
    """<p>The top 200 error results from the test set discrepancy report.</p>"""
    test_set_discrepancy_raw_output_url: NotRequired[
        "aws_sdk_lex_models_v2.types.presigned_s3_url.PresignedS3Url"
    ]
    """<p>Pre-signed Amazon S3 URL to download the test set discrepancy report.</p>"""
    failure_reasons: NotRequired[
        "aws_sdk_lex_models_v2.types.failure_reasons.FailureReasons"
    ]
    """<p>The failure report for the test set discrepancy report generation action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTestSetDiscrepancyReportResponse) -> dict:
    out: dict = {}
    if "test_set_discrepancy_report_id" in value:
        out["testSetDiscrepancyReportId"] = value["test_set_discrepancy_report_id"]
    if "test_set_id" in value:
        out["testSetId"] = value["test_set_id"]
    if "creation_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creationDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "target" in value:
        import aws_sdk_lex_models_v2.types.test_set_discrepancy_report_resource_target

        out["target"] = (
            aws_sdk_lex_models_v2.types.test_set_discrepancy_report_resource_target.serialize_json(
                value["target"]
            )
        )
    if "test_set_discrepancy_report_status" in value:
        import aws_sdk_lex_models_v2.types.test_set_discrepancy_report_status

        out["testSetDiscrepancyReportStatus"] = (
            aws_sdk_lex_models_v2.types.test_set_discrepancy_report_status.serialize_json(
                value["test_set_discrepancy_report_status"]
            )
        )
    if "last_updated_data_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["lastUpdatedDataTime"] = (
            aws_sdk_lex_models_v2.types.timestamp.serialize_json(
                value["last_updated_data_time"]
            )
        )
    if "test_set_discrepancy_top_errors" in value:
        import aws_sdk_lex_models_v2.types.test_set_discrepancy_errors

        out["testSetDiscrepancyTopErrors"] = (
            aws_sdk_lex_models_v2.types.test_set_discrepancy_errors.serialize_json(
                value["test_set_discrepancy_top_errors"]
            )
        )
    if "test_set_discrepancy_raw_output_url" in value:
        out["testSetDiscrepancyRawOutputUrl"] = value[
            "test_set_discrepancy_raw_output_url"
        ]
    if "failure_reasons" in value:
        import aws_sdk_lex_models_v2.types.failure_reasons

        out["failureReasons"] = (
            aws_sdk_lex_models_v2.types.failure_reasons.serialize_json(
                value["failure_reasons"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeTestSetDiscrepancyReportResponse:
    out: DescribeTestSetDiscrepancyReportResponse = {}  # type: ignore[typeddict-item]
    if "testSetDiscrepancyReportId" in data:
        out["test_set_discrepancy_report_id"] = data["testSetDiscrepancyReportId"]
    if "testSetId" in data:
        out["test_set_id"] = data["testSetId"]
    if "creationDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    if "target" in data:
        import aws_sdk_lex_models_v2.types.test_set_discrepancy_report_resource_target

        out["target"] = (
            aws_sdk_lex_models_v2.types.test_set_discrepancy_report_resource_target.deserialize_json(
                data["target"]
            )
        )
    if "testSetDiscrepancyReportStatus" in data:
        import aws_sdk_lex_models_v2.types.test_set_discrepancy_report_status

        out["test_set_discrepancy_report_status"] = (
            aws_sdk_lex_models_v2.types.test_set_discrepancy_report_status.deserialize_json(
                data["testSetDiscrepancyReportStatus"]
            )
        )
    if "lastUpdatedDataTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["last_updated_data_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDataTime"]
            )
        )
    if "testSetDiscrepancyTopErrors" in data:
        import aws_sdk_lex_models_v2.types.test_set_discrepancy_errors

        out["test_set_discrepancy_top_errors"] = (
            aws_sdk_lex_models_v2.types.test_set_discrepancy_errors.deserialize_json(
                data["testSetDiscrepancyTopErrors"]
            )
        )
    if "testSetDiscrepancyRawOutputUrl" in data:
        out["test_set_discrepancy_raw_output_url"] = data[
            "testSetDiscrepancyRawOutputUrl"
        ]
    if "failureReasons" in data:
        import aws_sdk_lex_models_v2.types.failure_reasons

        out["failure_reasons"] = (
            aws_sdk_lex_models_v2.types.failure_reasons.deserialize_json(
                data["failureReasons"]
            )
        )
    return out
