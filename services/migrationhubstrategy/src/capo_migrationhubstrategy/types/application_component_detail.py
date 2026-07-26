"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ApplicationComponentDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.antipattern_report_status
    import capo_migrationhubstrategy.types.app_type
    import capo_migrationhubstrategy.types.app_unit_error
    import capo_migrationhubstrategy.types.boolean
    import capo_migrationhubstrategy.types.database_config_detail
    import capo_migrationhubstrategy.types.inclusion_status
    import capo_migrationhubstrategy.types.list_antipattern_severity_summary
    import capo_migrationhubstrategy.types.recommendation_set
    import capo_migrationhubstrategy.types.resource_id
    import capo_migrationhubstrategy.types.resource_name
    import capo_migrationhubstrategy.types.resource_sub_type
    import capo_migrationhubstrategy.types.result_list
    import capo_migrationhubstrategy.types.runtime_analysis_status
    import capo_migrationhubstrategy.types.s3_object
    import capo_migrationhubstrategy.types.server_id
    import capo_migrationhubstrategy.types.source_code_repositories
    import capo_migrationhubstrategy.types.src_code_or_db_analysis_status
    import capo_migrationhubstrategy.types.status_message
    import capo_migrationhubstrategy.types.string
    import capo_migrationhubstrategy.types.time_stamp


class ApplicationComponentDetail(TypedDict, closed=True):
    id: NotRequired["capo_migrationhubstrategy.types.resource_id.ResourceId"]
    """<p> The ID of the application component. </p>"""
    name: NotRequired["capo_migrationhubstrategy.types.resource_name.ResourceName"]
    """<p> The name of application component. </p>"""
    recommendation_set: NotRequired[
        "capo_migrationhubstrategy.types.recommendation_set.RecommendationSet"
    ]
    """<p> The top recommendation set for the application component. </p>"""
    analysis_status: NotRequired[
        "capo_migrationhubstrategy.types.src_code_or_db_analysis_status.SrcCodeOrDbAnalysisStatus"
    ]
    """<p> The status of analysis, if the application component has source code or an associated database. </p>"""
    status_message: NotRequired[
        "capo_migrationhubstrategy.types.status_message.StatusMessage"
    ]
    """<p> A detailed description of the analysis status and any failure message. </p>"""
    list_antipattern_severity_summary: NotRequired[
        "capo_migrationhubstrategy.types.list_antipattern_severity_summary.ListAntipatternSeveritySummary"
    ]
    """<p> A list of anti-pattern severity summaries. </p>"""
    database_config_detail: NotRequired[
        "capo_migrationhubstrategy.types.database_config_detail.DatabaseConfigDetail"
    ]
    """<p> Configuration details for the database associated with the application component. </p>"""
    source_code_repositories: NotRequired[
        "capo_migrationhubstrategy.types.source_code_repositories.SourceCodeRepositories"
    ]
    """<p> Details about the source code repository associated with the application component. </p>"""
    app_type: NotRequired["capo_migrationhubstrategy.types.app_type.AppType"]
    """<p> The type of application component. </p>"""
    resource_sub_type: NotRequired[
        "capo_migrationhubstrategy.types.resource_sub_type.ResourceSubType"
    ]
    """<p> The application component subtype.</p>"""
    inclusion_status: NotRequired[
        "capo_migrationhubstrategy.types.inclusion_status.InclusionStatus"
    ]
    """<p> Indicates whether the application component has been included for server recommendation or not. </p>"""
    antipattern_report_s3_object: NotRequired[
        "capo_migrationhubstrategy.types.s3_object.S3Object"
    ]
    """<p> The S3 bucket name and the Amazon S3 key name for the anti-pattern report. </p>"""
    antipattern_report_status: NotRequired[
        "capo_migrationhubstrategy.types.antipattern_report_status.AntipatternReportStatus"
    ]
    """<p> The status of the anti-pattern report generation.</p>"""
    antipattern_report_status_message: NotRequired[
        "capo_migrationhubstrategy.types.status_message.StatusMessage"
    ]
    """<p> The status message for the anti-pattern. </p>"""
    os_version: NotRequired["capo_migrationhubstrategy.types.string.String"]
    """<p> OS version. </p>"""
    os_driver: NotRequired["capo_migrationhubstrategy.types.string.String"]
    """<p> OS driver. </p>"""
    last_analyzed_timestamp: NotRequired[
        "capo_migrationhubstrategy.types.time_stamp.TimeStamp"
    ]
    """<p> The timestamp of when the application component was assessed. </p>"""
    associated_server_id: NotRequired[
        "capo_migrationhubstrategy.types.server_id.ServerId"
    ]
    """<p> The ID of the server that the application component is running on. </p>"""
    more_server_association_exists: NotRequired[
        "capo_migrationhubstrategy.types.boolean.Boolean"
    ]
    """<p> Set to true if the application component is running on multiple servers.</p>"""
    runtime_status: NotRequired[
        "capo_migrationhubstrategy.types.runtime_analysis_status.RuntimeAnalysisStatus"
    ]
    """<p>The status of the application unit.</p>"""
    runtime_status_message: NotRequired[
        "capo_migrationhubstrategy.types.status_message.StatusMessage"
    ]
    """<p>The status message for the application unit.</p>"""
    app_unit_error: NotRequired[
        "capo_migrationhubstrategy.types.app_unit_error.AppUnitError"
    ]
    """<p>The error in the analysis of the source code or database.</p>"""
    result_list: NotRequired["capo_migrationhubstrategy.types.result_list.ResultList"]
    """<p>A list of the analysis results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationComponentDetail) -> dict:
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
    if "analysis_status" in value:
        out["analysisStatus"] = value["analysis_status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "list_antipattern_severity_summary" in value:
        import capo_migrationhubstrategy.types.list_antipattern_severity_summary

        out["listAntipatternSeveritySummary"] = (
            capo_migrationhubstrategy.types.list_antipattern_severity_summary.serialize_json(
                value["list_antipattern_severity_summary"]
            )
        )
    if "database_config_detail" in value:
        import capo_migrationhubstrategy.types.database_config_detail

        out["databaseConfigDetail"] = (
            capo_migrationhubstrategy.types.database_config_detail.serialize_json(
                value["database_config_detail"]
            )
        )
    if "source_code_repositories" in value:
        import capo_migrationhubstrategy.types.source_code_repositories

        out["sourceCodeRepositories"] = (
            capo_migrationhubstrategy.types.source_code_repositories.serialize_json(
                value["source_code_repositories"]
            )
        )
    if "app_type" in value:
        out["appType"] = value["app_type"]
    if "resource_sub_type" in value:
        out["resourceSubType"] = value["resource_sub_type"]
    if "inclusion_status" in value:
        out["inclusionStatus"] = value["inclusion_status"]
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
    if "os_version" in value:
        out["osVersion"] = value["os_version"]
    if "os_driver" in value:
        out["osDriver"] = value["os_driver"]
    if "last_analyzed_timestamp" in value:
        import capo_migrationhubstrategy.types.time_stamp

        out["lastAnalyzedTimestamp"] = (
            capo_migrationhubstrategy.types.time_stamp.serialize_json(
                value["last_analyzed_timestamp"]
            )
        )
    if "associated_server_id" in value:
        out["associatedServerId"] = value["associated_server_id"]
    if "more_server_association_exists" in value:
        out["moreServerAssociationExists"] = value["more_server_association_exists"]
    if "runtime_status" in value:
        out["runtimeStatus"] = value["runtime_status"]
    if "runtime_status_message" in value:
        out["runtimeStatusMessage"] = value["runtime_status_message"]
    if "app_unit_error" in value:
        import capo_migrationhubstrategy.types.app_unit_error

        out["appUnitError"] = (
            capo_migrationhubstrategy.types.app_unit_error.serialize_json(
                value["app_unit_error"]
            )
        )
    if "result_list" in value:
        import capo_migrationhubstrategy.types.result_list

        out["resultList"] = capo_migrationhubstrategy.types.result_list.serialize_json(
            value["result_list"]
        )
    return out


def deserialize_json(data: dict) -> ApplicationComponentDetail:
    out: ApplicationComponentDetail = {}  # type: ignore[typeddict-item]
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
    if "analysisStatus" in data:
        out["analysis_status"] = data["analysisStatus"]
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "listAntipatternSeveritySummary" in data:
        import capo_migrationhubstrategy.types.list_antipattern_severity_summary

        out["list_antipattern_severity_summary"] = (
            capo_migrationhubstrategy.types.list_antipattern_severity_summary.deserialize_json(
                data["listAntipatternSeveritySummary"]
            )
        )
    if "databaseConfigDetail" in data:
        import capo_migrationhubstrategy.types.database_config_detail

        out["database_config_detail"] = (
            capo_migrationhubstrategy.types.database_config_detail.deserialize_json(
                data["databaseConfigDetail"]
            )
        )
    if "sourceCodeRepositories" in data:
        import capo_migrationhubstrategy.types.source_code_repositories

        out["source_code_repositories"] = (
            capo_migrationhubstrategy.types.source_code_repositories.deserialize_json(
                data["sourceCodeRepositories"]
            )
        )
    if "appType" in data:
        out["app_type"] = data["appType"]
    if "resourceSubType" in data:
        out["resource_sub_type"] = data["resourceSubType"]
    if "inclusionStatus" in data:
        out["inclusion_status"] = data["inclusionStatus"]
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
    if "osVersion" in data:
        out["os_version"] = data["osVersion"]
    if "osDriver" in data:
        out["os_driver"] = data["osDriver"]
    if "lastAnalyzedTimestamp" in data:
        import capo_migrationhubstrategy.types.time_stamp

        out["last_analyzed_timestamp"] = (
            capo_migrationhubstrategy.types.time_stamp.deserialize_json(
                data["lastAnalyzedTimestamp"]
            )
        )
    if "associatedServerId" in data:
        out["associated_server_id"] = data["associatedServerId"]
    if "moreServerAssociationExists" in data:
        out["more_server_association_exists"] = data["moreServerAssociationExists"]
    if "runtimeStatus" in data:
        out["runtime_status"] = data["runtimeStatus"]
    if "runtimeStatusMessage" in data:
        out["runtime_status_message"] = data["runtimeStatusMessage"]
    if "appUnitError" in data:
        import capo_migrationhubstrategy.types.app_unit_error

        out["app_unit_error"] = (
            capo_migrationhubstrategy.types.app_unit_error.deserialize_json(
                data["appUnitError"]
            )
        )
    if "resultList" in data:
        import capo_migrationhubstrategy.types.result_list

        out["result_list"] = (
            capo_migrationhubstrategy.types.result_list.deserialize_json(
                data["resultList"]
            )
        )
    return out
