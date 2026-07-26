"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AssessmentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.antipattern_report_status
    import capo_migrationhubstrategy.types.list_antipattern_severity_summary
    import capo_migrationhubstrategy.types.list_application_component_status_summary
    import capo_migrationhubstrategy.types.list_application_component_summary
    import capo_migrationhubstrategy.types.list_server_status_summary
    import capo_migrationhubstrategy.types.list_server_summary
    import capo_migrationhubstrategy.types.list_strategy_summary
    import capo_migrationhubstrategy.types.s3_object
    import capo_migrationhubstrategy.types.status_message
    import capo_migrationhubstrategy.types.time_stamp


class AssessmentSummary(TypedDict, closed=True):
    list_server_strategy_summary: NotRequired[
        "capo_migrationhubstrategy.types.list_strategy_summary.ListStrategySummary"
    ]
    """<p> List of ServerStrategySummary. </p>"""
    list_application_component_strategy_summary: NotRequired[
        "capo_migrationhubstrategy.types.list_strategy_summary.ListStrategySummary"
    ]
    """<p> List of ApplicationComponentStrategySummary. </p>"""
    list_antipattern_severity_summary: NotRequired[
        "capo_migrationhubstrategy.types.list_antipattern_severity_summary.ListAntipatternSeveritySummary"
    ]
    """<p> List of AntipatternSeveritySummary. </p>"""
    list_application_component_summary: NotRequired[
        "capo_migrationhubstrategy.types.list_application_component_summary.ListApplicationComponentSummary"
    ]
    """<p> List of ApplicationComponentSummary. </p>"""
    list_server_summary: NotRequired[
        "capo_migrationhubstrategy.types.list_server_summary.ListServerSummary"
    ]
    """<p> List of ServerSummary. </p>"""
    antipattern_report_s3_object: NotRequired[
        "capo_migrationhubstrategy.types.s3_object.S3Object"
    ]
    """<p> The Amazon S3 object containing the anti-pattern report. </p>"""
    antipattern_report_status: NotRequired[
        "capo_migrationhubstrategy.types.antipattern_report_status.AntipatternReportStatus"
    ]
    """<p> The status of the anti-pattern report. </p>"""
    antipattern_report_status_message: NotRequired[
        "capo_migrationhubstrategy.types.status_message.StatusMessage"
    ]
    """<p> The status message of the anti-pattern report. </p>"""
    last_analyzed_timestamp: NotRequired[
        "capo_migrationhubstrategy.types.time_stamp.TimeStamp"
    ]
    """<p> The time the assessment was performed. </p>"""
    list_application_component_status_summary: NotRequired[
        "capo_migrationhubstrategy.types.list_application_component_status_summary.ListApplicationComponentStatusSummary"
    ]
    """<p>List of status summaries of the analyzed application components.</p>"""
    list_server_status_summary: NotRequired[
        "capo_migrationhubstrategy.types.list_server_status_summary.ListServerStatusSummary"
    ]
    """<p>List of status summaries of the analyzed servers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentSummary) -> dict:
    out: dict = {}
    if "list_server_strategy_summary" in value:
        import capo_migrationhubstrategy.types.list_strategy_summary

        out["listServerStrategySummary"] = (
            capo_migrationhubstrategy.types.list_strategy_summary.serialize_json(
                value["list_server_strategy_summary"]
            )
        )
    if "list_application_component_strategy_summary" in value:
        import capo_migrationhubstrategy.types.list_strategy_summary

        out["listApplicationComponentStrategySummary"] = (
            capo_migrationhubstrategy.types.list_strategy_summary.serialize_json(
                value["list_application_component_strategy_summary"]
            )
        )
    if "list_antipattern_severity_summary" in value:
        import capo_migrationhubstrategy.types.list_antipattern_severity_summary

        out["listAntipatternSeveritySummary"] = (
            capo_migrationhubstrategy.types.list_antipattern_severity_summary.serialize_json(
                value["list_antipattern_severity_summary"]
            )
        )
    if "list_application_component_summary" in value:
        import capo_migrationhubstrategy.types.list_application_component_summary

        out["listApplicationComponentSummary"] = (
            capo_migrationhubstrategy.types.list_application_component_summary.serialize_json(
                value["list_application_component_summary"]
            )
        )
    if "list_server_summary" in value:
        import capo_migrationhubstrategy.types.list_server_summary

        out["listServerSummary"] = (
            capo_migrationhubstrategy.types.list_server_summary.serialize_json(
                value["list_server_summary"]
            )
        )
    if "antipattern_report_s3_object" in value:
        import capo_migrationhubstrategy.types.s3_object

        out["antipatternReportS3Object"] = (
            capo_migrationhubstrategy.types.s3_object.serialize_json(
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
        import capo_migrationhubstrategy.types.time_stamp

        out["lastAnalyzedTimestamp"] = (
            capo_migrationhubstrategy.types.time_stamp.serialize_json(
                value["last_analyzed_timestamp"]
            )
        )
    if "list_application_component_status_summary" in value:
        import capo_migrationhubstrategy.types.list_application_component_status_summary

        out["listApplicationComponentStatusSummary"] = (
            capo_migrationhubstrategy.types.list_application_component_status_summary.serialize_json(
                value["list_application_component_status_summary"]
            )
        )
    if "list_server_status_summary" in value:
        import capo_migrationhubstrategy.types.list_server_status_summary

        out["listServerStatusSummary"] = (
            capo_migrationhubstrategy.types.list_server_status_summary.serialize_json(
                value["list_server_status_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssessmentSummary:
    out: AssessmentSummary = {}  # type: ignore[typeddict-item]
    if "listServerStrategySummary" in data:
        import capo_migrationhubstrategy.types.list_strategy_summary

        out["list_server_strategy_summary"] = (
            capo_migrationhubstrategy.types.list_strategy_summary.deserialize_json(
                data["listServerStrategySummary"]
            )
        )
    if "listApplicationComponentStrategySummary" in data:
        import capo_migrationhubstrategy.types.list_strategy_summary

        out["list_application_component_strategy_summary"] = (
            capo_migrationhubstrategy.types.list_strategy_summary.deserialize_json(
                data["listApplicationComponentStrategySummary"]
            )
        )
    if "listAntipatternSeveritySummary" in data:
        import capo_migrationhubstrategy.types.list_antipattern_severity_summary

        out["list_antipattern_severity_summary"] = (
            capo_migrationhubstrategy.types.list_antipattern_severity_summary.deserialize_json(
                data["listAntipatternSeveritySummary"]
            )
        )
    if "listApplicationComponentSummary" in data:
        import capo_migrationhubstrategy.types.list_application_component_summary

        out["list_application_component_summary"] = (
            capo_migrationhubstrategy.types.list_application_component_summary.deserialize_json(
                data["listApplicationComponentSummary"]
            )
        )
    if "listServerSummary" in data:
        import capo_migrationhubstrategy.types.list_server_summary

        out["list_server_summary"] = (
            capo_migrationhubstrategy.types.list_server_summary.deserialize_json(
                data["listServerSummary"]
            )
        )
    if "antipatternReportS3Object" in data:
        import capo_migrationhubstrategy.types.s3_object

        out["antipattern_report_s3_object"] = (
            capo_migrationhubstrategy.types.s3_object.deserialize_json(
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
        import capo_migrationhubstrategy.types.time_stamp

        out["last_analyzed_timestamp"] = (
            capo_migrationhubstrategy.types.time_stamp.deserialize_json(
                data["lastAnalyzedTimestamp"]
            )
        )
    if "listApplicationComponentStatusSummary" in data:
        import capo_migrationhubstrategy.types.list_application_component_status_summary

        out["list_application_component_status_summary"] = (
            capo_migrationhubstrategy.types.list_application_component_status_summary.deserialize_json(
                data["listApplicationComponentStatusSummary"]
            )
        )
    if "listServerStatusSummary" in data:
        import capo_migrationhubstrategy.types.list_server_status_summary

        out["list_server_status_summary"] = (
            capo_migrationhubstrategy.types.list_server_status_summary.deserialize_json(
                data["listServerStatusSummary"]
            )
        )
    return out
