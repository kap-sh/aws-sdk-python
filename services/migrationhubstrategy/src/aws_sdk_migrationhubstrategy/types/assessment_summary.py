"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AssessmentSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.antipattern_report_status
    import aws_sdk_migrationhubstrategy.types.list_antipattern_severity_summary
    import aws_sdk_migrationhubstrategy.types.list_application_component_status_summary
    import aws_sdk_migrationhubstrategy.types.list_application_component_summary
    import aws_sdk_migrationhubstrategy.types.list_server_status_summary
    import aws_sdk_migrationhubstrategy.types.list_server_summary
    import aws_sdk_migrationhubstrategy.types.list_strategy_summary
    import aws_sdk_migrationhubstrategy.types.s3_object
    import aws_sdk_migrationhubstrategy.types.status_message
    import aws_sdk_migrationhubstrategy.types.time_stamp


class AssessmentSummary(TypedDict):
    list_server_strategy_summary: NotRequired[
        "aws_sdk_migrationhubstrategy.types.list_strategy_summary.ListStrategySummary"
    ]
    """<p> List of ServerStrategySummary. </p>"""
    list_application_component_strategy_summary: NotRequired[
        "aws_sdk_migrationhubstrategy.types.list_strategy_summary.ListStrategySummary"
    ]
    """<p> List of ApplicationComponentStrategySummary. </p>"""
    list_antipattern_severity_summary: NotRequired[
        "aws_sdk_migrationhubstrategy.types.list_antipattern_severity_summary.ListAntipatternSeveritySummary"
    ]
    """<p> List of AntipatternSeveritySummary. </p>"""
    list_application_component_summary: NotRequired[
        "aws_sdk_migrationhubstrategy.types.list_application_component_summary.ListApplicationComponentSummary"
    ]
    """<p> List of ApplicationComponentSummary. </p>"""
    list_server_summary: NotRequired[
        "aws_sdk_migrationhubstrategy.types.list_server_summary.ListServerSummary"
    ]
    """<p> List of ServerSummary. </p>"""
    antipattern_report_s3_object: NotRequired[
        "aws_sdk_migrationhubstrategy.types.s3_object.S3Object"
    ]
    """<p> The Amazon S3 object containing the anti-pattern report. </p>"""
    antipattern_report_status: NotRequired[
        "aws_sdk_migrationhubstrategy.types.antipattern_report_status.AntipatternReportStatus"
    ]
    """<p> The status of the anti-pattern report. </p>"""
    antipattern_report_status_message: NotRequired[
        "aws_sdk_migrationhubstrategy.types.status_message.StatusMessage"
    ]
    """<p> The status message of the anti-pattern report. </p>"""
    last_analyzed_timestamp: NotRequired[
        "aws_sdk_migrationhubstrategy.types.time_stamp.TimeStamp"
    ]
    """<p> The time the assessment was performed. </p>"""
    list_application_component_status_summary: NotRequired[
        "aws_sdk_migrationhubstrategy.types.list_application_component_status_summary.ListApplicationComponentStatusSummary"
    ]
    """<p>List of status summaries of the analyzed application components.</p>"""
    list_server_status_summary: NotRequired[
        "aws_sdk_migrationhubstrategy.types.list_server_status_summary.ListServerStatusSummary"
    ]
    """<p>List of status summaries of the analyzed servers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentSummary) -> dict:
    out: dict = {}
    if "list_server_strategy_summary" in value:
        import aws_sdk_migrationhubstrategy.types.list_strategy_summary

        out["listServerStrategySummary"] = (
            aws_sdk_migrationhubstrategy.types.list_strategy_summary.serialize_json(
                value["list_server_strategy_summary"]
            )
        )
    if "list_application_component_strategy_summary" in value:
        import aws_sdk_migrationhubstrategy.types.list_strategy_summary

        out["listApplicationComponentStrategySummary"] = (
            aws_sdk_migrationhubstrategy.types.list_strategy_summary.serialize_json(
                value["list_application_component_strategy_summary"]
            )
        )
    if "list_antipattern_severity_summary" in value:
        import aws_sdk_migrationhubstrategy.types.list_antipattern_severity_summary

        out["listAntipatternSeveritySummary"] = (
            aws_sdk_migrationhubstrategy.types.list_antipattern_severity_summary.serialize_json(
                value["list_antipattern_severity_summary"]
            )
        )
    if "list_application_component_summary" in value:
        import aws_sdk_migrationhubstrategy.types.list_application_component_summary

        out["listApplicationComponentSummary"] = (
            aws_sdk_migrationhubstrategy.types.list_application_component_summary.serialize_json(
                value["list_application_component_summary"]
            )
        )
    if "list_server_summary" in value:
        import aws_sdk_migrationhubstrategy.types.list_server_summary

        out["listServerSummary"] = (
            aws_sdk_migrationhubstrategy.types.list_server_summary.serialize_json(
                value["list_server_summary"]
            )
        )
    if "antipattern_report_s3_object" in value:
        import aws_sdk_migrationhubstrategy.types.s3_object

        out["antipatternReportS3Object"] = (
            aws_sdk_migrationhubstrategy.types.s3_object.serialize_json(
                value["antipattern_report_s3_object"]
            )
        )
    if "antipattern_report_status" in value:
        out["antipatternReportStatus"] = value["antipattern_report_status"]
    if "antipattern_report_status_message" in value:
        out["antipatternReportStatusMessage"] = value[
            "antipattern_report_status_message"
        ]
    if "last_analyzed_timestamp" in value:
        import aws_sdk_migrationhubstrategy.types.time_stamp

        out["lastAnalyzedTimestamp"] = (
            aws_sdk_migrationhubstrategy.types.time_stamp.serialize_json(
                value["last_analyzed_timestamp"]
            )
        )
    if "list_application_component_status_summary" in value:
        import aws_sdk_migrationhubstrategy.types.list_application_component_status_summary

        out["listApplicationComponentStatusSummary"] = (
            aws_sdk_migrationhubstrategy.types.list_application_component_status_summary.serialize_json(
                value["list_application_component_status_summary"]
            )
        )
    if "list_server_status_summary" in value:
        import aws_sdk_migrationhubstrategy.types.list_server_status_summary

        out["listServerStatusSummary"] = (
            aws_sdk_migrationhubstrategy.types.list_server_status_summary.serialize_json(
                value["list_server_status_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssessmentSummary:
    out: AssessmentSummary = {}  # type: ignore[typeddict-item]
    if "listServerStrategySummary" in data:
        import aws_sdk_migrationhubstrategy.types.list_strategy_summary

        out["list_server_strategy_summary"] = (
            aws_sdk_migrationhubstrategy.types.list_strategy_summary.deserialize_json(
                data["listServerStrategySummary"]
            )
        )
    if "listApplicationComponentStrategySummary" in data:
        import aws_sdk_migrationhubstrategy.types.list_strategy_summary

        out["list_application_component_strategy_summary"] = (
            aws_sdk_migrationhubstrategy.types.list_strategy_summary.deserialize_json(
                data["listApplicationComponentStrategySummary"]
            )
        )
    if "listAntipatternSeveritySummary" in data:
        import aws_sdk_migrationhubstrategy.types.list_antipattern_severity_summary

        out["list_antipattern_severity_summary"] = (
            aws_sdk_migrationhubstrategy.types.list_antipattern_severity_summary.deserialize_json(
                data["listAntipatternSeveritySummary"]
            )
        )
    if "listApplicationComponentSummary" in data:
        import aws_sdk_migrationhubstrategy.types.list_application_component_summary

        out["list_application_component_summary"] = (
            aws_sdk_migrationhubstrategy.types.list_application_component_summary.deserialize_json(
                data["listApplicationComponentSummary"]
            )
        )
    if "listServerSummary" in data:
        import aws_sdk_migrationhubstrategy.types.list_server_summary

        out["list_server_summary"] = (
            aws_sdk_migrationhubstrategy.types.list_server_summary.deserialize_json(
                data["listServerSummary"]
            )
        )
    if "antipatternReportS3Object" in data:
        import aws_sdk_migrationhubstrategy.types.s3_object

        out["antipattern_report_s3_object"] = (
            aws_sdk_migrationhubstrategy.types.s3_object.deserialize_json(
                data["antipatternReportS3Object"]
            )
        )
    if "antipatternReportStatus" in data:
        out["antipattern_report_status"] = data["antipatternReportStatus"]
    if "antipatternReportStatusMessage" in data:
        out["antipattern_report_status_message"] = data[
            "antipatternReportStatusMessage"
        ]
    if "lastAnalyzedTimestamp" in data:
        import aws_sdk_migrationhubstrategy.types.time_stamp

        out["last_analyzed_timestamp"] = (
            aws_sdk_migrationhubstrategy.types.time_stamp.deserialize_json(
                data["lastAnalyzedTimestamp"]
            )
        )
    if "listApplicationComponentStatusSummary" in data:
        import aws_sdk_migrationhubstrategy.types.list_application_component_status_summary

        out["list_application_component_status_summary"] = (
            aws_sdk_migrationhubstrategy.types.list_application_component_status_summary.deserialize_json(
                data["listApplicationComponentStatusSummary"]
            )
        )
    if "listServerStatusSummary" in data:
        import aws_sdk_migrationhubstrategy.types.list_server_status_summary

        out["list_server_status_summary"] = (
            aws_sdk_migrationhubstrategy.types.list_server_status_summary.deserialize_json(
                data["listServerStatusSummary"]
            )
        )
    return out
