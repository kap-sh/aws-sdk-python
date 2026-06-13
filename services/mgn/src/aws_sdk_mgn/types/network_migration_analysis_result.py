"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationAnalysisResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.analyzer_type
    import aws_sdk_mgn.types.network_migration_analysis_result_source
    import aws_sdk_mgn.types.network_migration_analysis_result_status
    import aws_sdk_mgn.types.network_migration_analysis_result_target
    import aws_sdk_mgn.types.network_migration_definition_id
    import aws_sdk_mgn.types.network_migration_execution_id
    import aws_sdk_mgn.types.network_migration_job_id


class NetworkMigrationAnalysisResult(TypedDict):
    job_id: NotRequired[
        "aws_sdk_mgn.types.network_migration_job_id.NetworkMigrationJobID"
    ]
    """<p>The unique identifier of the analysis job that generated this result.</p>"""
    network_migration_execution_id: NotRequired[
        "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    ]
    """<p>The unique identifier of the network migration execution.</p>"""
    network_migration_definition_id: NotRequired[
        "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    ]
    """<p>The unique identifier of the network migration definition.</p>"""
    analyzer_type: NotRequired["aws_sdk_mgn.types.analyzer_type.AnalyzerType"]
    """<p>The type of analyzer that generated this result.</p>"""
    source: NotRequired[
        "aws_sdk_mgn.types.network_migration_analysis_result_source.NetworkMigrationAnalysisResultSource"
    ]
    """<p>The source resource that was analyzed.</p>"""
    target: NotRequired[
        "aws_sdk_mgn.types.network_migration_analysis_result_target.NetworkMigrationAnalysisResultTarget"
    ]
    """<p>The target resource in the analysis.</p>"""
    status: NotRequired[
        "aws_sdk_mgn.types.network_migration_analysis_result_status.NetworkMigrationAnalysisResultStatus"
    ]
    """<p>The status of the analysis result.</p>"""
    analysis_result: NotRequired["str"]
    """<p>The detailed analysis findings and recommendations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationAnalysisResult) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobID"] = value["job_id"]
    if "network_migration_execution_id" in value:
        out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    if "network_migration_definition_id" in value:
        out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "analyzer_type" in value:
        out["analyzerType"] = value["analyzer_type"]
    if "source" in value:
        import aws_sdk_mgn.types.network_migration_analysis_result_source

        out["source"] = (
            aws_sdk_mgn.types.network_migration_analysis_result_source.serialize_json(
                value["source"]
            )
        )
    if "target" in value:
        import aws_sdk_mgn.types.network_migration_analysis_result_target

        out["target"] = (
            aws_sdk_mgn.types.network_migration_analysis_result_target.serialize_json(
                value["target"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "analysis_result" in value:
        out["analysisResult"] = value["analysis_result"]
    return out


def deserialize_json(data: dict) -> NetworkMigrationAnalysisResult:
    out: NetworkMigrationAnalysisResult = {}  # type: ignore[typeddict-item]
    if "jobID" in data:
        out["job_id"] = data["jobID"]
    if "networkMigrationExecutionID" in data:
        out["network_migration_execution_id"] = data["networkMigrationExecutionID"]
    if "networkMigrationDefinitionID" in data:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    if "analyzerType" in data:
        out["analyzer_type"] = data["analyzerType"]
    if "source" in data:
        import aws_sdk_mgn.types.network_migration_analysis_result_source

        out["source"] = (
            aws_sdk_mgn.types.network_migration_analysis_result_source.deserialize_json(
                data["source"]
            )
        )
    if "target" in data:
        import aws_sdk_mgn.types.network_migration_analysis_result_target

        out["target"] = (
            aws_sdk_mgn.types.network_migration_analysis_result_target.deserialize_json(
                data["target"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    if "analysisResult" in data:
        out["analysis_result"] = data["analysisResult"]
    return out
