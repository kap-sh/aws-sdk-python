"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ServerDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.antipattern_report_status
    import capo_migrationhubstrategy.types.list_antipattern_severity_summary
    import capo_migrationhubstrategy.types.list_strategy_summary
    import capo_migrationhubstrategy.types.recommendation_set
    import capo_migrationhubstrategy.types.resource_id
    import capo_migrationhubstrategy.types.resource_name
    import capo_migrationhubstrategy.types.run_time_assessment_status
    import capo_migrationhubstrategy.types.s3_object
    import capo_migrationhubstrategy.types.server_error
    import capo_migrationhubstrategy.types.status_message
    import capo_migrationhubstrategy.types.string
    import capo_migrationhubstrategy.types.system_info
    import capo_migrationhubstrategy.types.time_stamp


class ServerDetail(TypedDict, closed=True):
    id: NotRequired["capo_migrationhubstrategy.types.resource_id.ResourceId"]
    """<p> The server ID. </p>"""
    name: NotRequired["capo_migrationhubstrategy.types.resource_name.ResourceName"]
    """<p> The name of the server. </p>"""
    recommendation_set: NotRequired[
        "capo_migrationhubstrategy.types.recommendation_set.RecommendationSet"
    ]
    """<p> A set of recommendations. </p>"""
    data_collection_status: NotRequired[
        "capo_migrationhubstrategy.types.run_time_assessment_status.RunTimeAssessmentStatus"
    ]
    """<p> The status of assessment for the server. </p>"""
    status_message: NotRequired[
        "capo_migrationhubstrategy.types.status_message.StatusMessage"
    ]
    """<p> A message about the status of data collection, which contains detailed descriptions of any error messages. </p>"""
    list_antipattern_severity_summary: NotRequired[
        "capo_migrationhubstrategy.types.list_antipattern_severity_summary.ListAntipatternSeveritySummary"
    ]
    """<p> A list of anti-pattern severity summaries. </p>"""
    system_info: NotRequired["capo_migrationhubstrategy.types.system_info.SystemInfo"]
    """<p> System information about the server. </p>"""
    application_component_strategy_summary: NotRequired[
        "capo_migrationhubstrategy.types.list_strategy_summary.ListStrategySummary"
    ]
    """<p> A list of strategy summaries. </p>"""
    antipattern_report_s3_object: NotRequired[
        "capo_migrationhubstrategy.types.s3_object.S3Object"
    ]
    """<p> The S3 bucket name and Amazon S3 key name for anti-pattern report. </p>"""
    antipattern_report_status: NotRequired[
        "capo_migrationhubstrategy.types.antipattern_report_status.AntipatternReportStatus"
    ]
    """<p> The status of the anti-pattern report generation. </p>"""
    antipattern_report_status_message: NotRequired[
        "capo_migrationhubstrategy.types.status_message.StatusMessage"
    ]
    """<p> A message about the status of the anti-pattern report generation. </p>"""
    server_type: NotRequired["capo_migrationhubstrategy.types.string.String"]
    """<p> The type of server. </p>"""
    last_analyzed_timestamp: NotRequired[
        "capo_migrationhubstrategy.types.time_stamp.TimeStamp"
    ]
    """<p> The timestamp of when the server was assessed. </p>"""
    server_error: NotRequired[
        "capo_migrationhubstrategy.types.server_error.ServerError"
    ]
    """<p>The error in server analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "recommendation_set" in value:
        import capo_migrationhubstrategy.types.recommendation_set

        out["recommendationSet"] = (
            capo_migrationhubstrategy.types.recommendation_set.serialize_json(
                value["recommendation_set"]
            )
        )
    if "data_collection_status" in value:
        out["dataCollectionStatus"] = value["data_collection_status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "list_antipattern_severity_summary" in value:
        import capo_migrationhubstrategy.types.list_antipattern_severity_summary

        out["listAntipatternSeveritySummary"] = (
            capo_migrationhubstrategy.types.list_antipattern_severity_summary.serialize_json(
                value["list_antipattern_severity_summary"]
            )
        )
    if "system_info" in value:
        import capo_migrationhubstrategy.types.system_info

        out["systemInfo"] = capo_migrationhubstrategy.types.system_info.serialize_json(
            value["system_info"]
        )
    if "application_component_strategy_summary" in value:
        import capo_migrationhubstrategy.types.list_strategy_summary

        out["applicationComponentStrategySummary"] = (
            capo_migrationhubstrategy.types.list_strategy_summary.serialize_json(
                value["application_component_strategy_summary"]
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
    if "server_type" in value:
        out["serverType"] = value["server_type"]
    if "last_analyzed_timestamp" in value:
        import capo_migrationhubstrategy.types.time_stamp

        out["lastAnalyzedTimestamp"] = (
            capo_migrationhubstrategy.types.time_stamp.serialize_json(
                value["last_analyzed_timestamp"]
            )
        )
    if "server_error" in value:
        import capo_migrationhubstrategy.types.server_error

        out["serverError"] = (
            capo_migrationhubstrategy.types.server_error.serialize_json(
                value["server_error"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServerDetail:
    out: ServerDetail = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "recommendationSet" in data:
        import capo_migrationhubstrategy.types.recommendation_set

        out["recommendation_set"] = (
            capo_migrationhubstrategy.types.recommendation_set.deserialize_json(
                data["recommendationSet"]
            )
        )
    if "dataCollectionStatus" in data:
        out["data_collection_status"] = data["dataCollectionStatus"]
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "listAntipatternSeveritySummary" in data:
        import capo_migrationhubstrategy.types.list_antipattern_severity_summary

        out["list_antipattern_severity_summary"] = (
            capo_migrationhubstrategy.types.list_antipattern_severity_summary.deserialize_json(
                data["listAntipatternSeveritySummary"]
            )
        )
    if "systemInfo" in data:
        import capo_migrationhubstrategy.types.system_info

        out["system_info"] = (
            capo_migrationhubstrategy.types.system_info.deserialize_json(
                data["systemInfo"]
            )
        )
    if "applicationComponentStrategySummary" in data:
        import capo_migrationhubstrategy.types.list_strategy_summary

        out["application_component_strategy_summary"] = (
            capo_migrationhubstrategy.types.list_strategy_summary.deserialize_json(
                data["applicationComponentStrategySummary"]
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
    if "serverType" in data:
        out["server_type"] = data["serverType"]
    if "lastAnalyzedTimestamp" in data:
        import capo_migrationhubstrategy.types.time_stamp

        out["last_analyzed_timestamp"] = (
            capo_migrationhubstrategy.types.time_stamp.deserialize_json(
                data["lastAnalyzedTimestamp"]
            )
        )
    if "serverError" in data:
        import capo_migrationhubstrategy.types.server_error

        out["server_error"] = (
            capo_migrationhubstrategy.types.server_error.deserialize_json(
                data["serverError"]
            )
        )
    return out
