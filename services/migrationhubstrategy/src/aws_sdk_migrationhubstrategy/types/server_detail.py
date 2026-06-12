"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ServerDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.antipattern_report_status
    import aws_sdk_migrationhubstrategy.types.list_antipattern_severity_summary
    import aws_sdk_migrationhubstrategy.types.list_strategy_summary
    import aws_sdk_migrationhubstrategy.types.recommendation_set
    import aws_sdk_migrationhubstrategy.types.resource_id
    import aws_sdk_migrationhubstrategy.types.resource_name
    import aws_sdk_migrationhubstrategy.types.run_time_assessment_status
    import aws_sdk_migrationhubstrategy.types.s3_object
    import aws_sdk_migrationhubstrategy.types.server_error
    import aws_sdk_migrationhubstrategy.types.status_message
    import aws_sdk_migrationhubstrategy.types.string
    import aws_sdk_migrationhubstrategy.types.system_info
    import aws_sdk_migrationhubstrategy.types.time_stamp


class ServerDetail(TypedDict):
    id: NotRequired["aws_sdk_migrationhubstrategy.types.resource_id.ResourceId"]
    """<p> The server ID. </p>"""
    name: NotRequired["aws_sdk_migrationhubstrategy.types.resource_name.ResourceName"]
    """<p> The name of the server. </p>"""
    recommendation_set: NotRequired[
        "aws_sdk_migrationhubstrategy.types.recommendation_set.RecommendationSet"
    ]
    """<p> A set of recommendations. </p>"""
    data_collection_status: NotRequired[
        "aws_sdk_migrationhubstrategy.types.run_time_assessment_status.RunTimeAssessmentStatus"
    ]
    """<p> The status of assessment for the server. </p>"""
    status_message: NotRequired[
        "aws_sdk_migrationhubstrategy.types.status_message.StatusMessage"
    ]
    """<p> A message about the status of data collection, which contains detailed descriptions of any error messages. </p>"""
    list_antipattern_severity_summary: NotRequired[
        "aws_sdk_migrationhubstrategy.types.list_antipattern_severity_summary.ListAntipatternSeveritySummary"
    ]
    """<p> A list of anti-pattern severity summaries. </p>"""
    system_info: NotRequired[
        "aws_sdk_migrationhubstrategy.types.system_info.SystemInfo"
    ]
    """<p> System information about the server. </p>"""
    application_component_strategy_summary: NotRequired[
        "aws_sdk_migrationhubstrategy.types.list_strategy_summary.ListStrategySummary"
    ]
    """<p> A list of strategy summaries. </p>"""
    antipattern_report_s3_object: NotRequired[
        "aws_sdk_migrationhubstrategy.types.s3_object.S3Object"
    ]
    """<p> The S3 bucket name and Amazon S3 key name for anti-pattern report. </p>"""
    antipattern_report_status: NotRequired[
        "aws_sdk_migrationhubstrategy.types.antipattern_report_status.AntipatternReportStatus"
    ]
    """<p> The status of the anti-pattern report generation. </p>"""
    antipattern_report_status_message: NotRequired[
        "aws_sdk_migrationhubstrategy.types.status_message.StatusMessage"
    ]
    """<p> A message about the status of the anti-pattern report generation. </p>"""
    server_type: NotRequired["aws_sdk_migrationhubstrategy.types.string.String"]
    """<p> The type of server. </p>"""
    last_analyzed_timestamp: NotRequired[
        "aws_sdk_migrationhubstrategy.types.time_stamp.TimeStamp"
    ]
    """<p> The timestamp of when the server was assessed. </p>"""
    server_error: NotRequired[
        "aws_sdk_migrationhubstrategy.types.server_error.ServerError"
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
        import aws_sdk_migrationhubstrategy.types.recommendation_set

        out["recommendationSet"] = (
            aws_sdk_migrationhubstrategy.types.recommendation_set.serialize_json(
                value["recommendation_set"]
            )
        )
    if "data_collection_status" in value:
        out["dataCollectionStatus"] = value["data_collection_status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "list_antipattern_severity_summary" in value:
        import aws_sdk_migrationhubstrategy.types.list_antipattern_severity_summary

        out["listAntipatternSeveritySummary"] = (
            aws_sdk_migrationhubstrategy.types.list_antipattern_severity_summary.serialize_json(
                value["list_antipattern_severity_summary"]
            )
        )
    if "system_info" in value:
        import aws_sdk_migrationhubstrategy.types.system_info

        out["systemInfo"] = (
            aws_sdk_migrationhubstrategy.types.system_info.serialize_json(
                value["system_info"]
            )
        )
    if "application_component_strategy_summary" in value:
        import aws_sdk_migrationhubstrategy.types.list_strategy_summary

        out["applicationComponentStrategySummary"] = (
            aws_sdk_migrationhubstrategy.types.list_strategy_summary.serialize_json(
                value["application_component_strategy_summary"]
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
    if "server_type" in value:
        out["serverType"] = value["server_type"]
    if "last_analyzed_timestamp" in value:
        import aws_sdk_migrationhubstrategy.types.time_stamp

        out["lastAnalyzedTimestamp"] = (
            aws_sdk_migrationhubstrategy.types.time_stamp.serialize_json(
                value["last_analyzed_timestamp"]
            )
        )
    if "server_error" in value:
        import aws_sdk_migrationhubstrategy.types.server_error

        out["serverError"] = (
            aws_sdk_migrationhubstrategy.types.server_error.serialize_json(
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
        import aws_sdk_migrationhubstrategy.types.recommendation_set

        out["recommendation_set"] = (
            aws_sdk_migrationhubstrategy.types.recommendation_set.deserialize_json(
                data["recommendationSet"]
            )
        )
    if "dataCollectionStatus" in data:
        out["data_collection_status"] = data["dataCollectionStatus"]
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "listAntipatternSeveritySummary" in data:
        import aws_sdk_migrationhubstrategy.types.list_antipattern_severity_summary

        out["list_antipattern_severity_summary"] = (
            aws_sdk_migrationhubstrategy.types.list_antipattern_severity_summary.deserialize_json(
                data["listAntipatternSeveritySummary"]
            )
        )
    if "systemInfo" in data:
        import aws_sdk_migrationhubstrategy.types.system_info

        out["system_info"] = (
            aws_sdk_migrationhubstrategy.types.system_info.deserialize_json(
                data["systemInfo"]
            )
        )
    if "applicationComponentStrategySummary" in data:
        import aws_sdk_migrationhubstrategy.types.list_strategy_summary

        out["application_component_strategy_summary"] = (
            aws_sdk_migrationhubstrategy.types.list_strategy_summary.deserialize_json(
                data["applicationComponentStrategySummary"]
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
    if "serverType" in data:
        out["server_type"] = data["serverType"]
    if "lastAnalyzedTimestamp" in data:
        import aws_sdk_migrationhubstrategy.types.time_stamp

        out["last_analyzed_timestamp"] = (
            aws_sdk_migrationhubstrategy.types.time_stamp.deserialize_json(
                data["lastAnalyzedTimestamp"]
            )
        )
    if "serverError" in data:
        import aws_sdk_migrationhubstrategy.types.server_error

        out["server_error"] = (
            aws_sdk_migrationhubstrategy.types.server_error.deserialize_json(
                data["serverError"]
            )
        )
    return out
