"""Generated from Smithy shape ``com.amazonaws.glue#GetDataQualityRuleRecommendationRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_ruleset_string
    import capo_glue.types.data_source
    import capo_glue.types.execution_time
    import capo_glue.types.generic_string
    import capo_glue.types.hash_string
    import capo_glue.types.name_string
    import capo_glue.types.nullable_integer
    import capo_glue.types.role_string
    import capo_glue.types.task_status_type
    import capo_glue.types.timeout
    import capo_glue.types.timestamp


class GetDataQualityRuleRecommendationRunResponse(TypedDict, closed=True):
    run_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The unique run identifier associated with this run.</p>"""
    data_source: NotRequired["capo_glue.types.data_source.DataSource"]
    """<p>The data source (an Glue table) associated with this run.</p>"""
    role: NotRequired["capo_glue.types.role_string.RoleString"]
    """<p>An IAM role supplied to encrypt the results of the run.</p>"""
    number_of_workers: NotRequired["capo_glue.types.nullable_integer.NullableInteger"]
    """<p>The number of <code>G.1X</code> workers to be used in the run. The default is 5.</p>"""
    timeout: NotRequired["capo_glue.types.timeout.Timeout"]
    """<p>The timeout for a run in minutes. This is the maximum time that a run can consume resources before it is terminated and enters <code>TIMEOUT</code> status. The default is 2,880 minutes (48 hours).</p>"""
    status: NotRequired["capo_glue.types.task_status_type.TaskStatusType"]
    """<p>The status for this run.</p>"""
    error_string: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The error strings that are associated with the run.</p>"""
    started_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The date and time when this run started.</p>"""
    last_modified_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>A timestamp. The last point in time when this data quality rule recommendation run was modified.</p>"""
    completed_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The date and time when this run was completed.</p>"""
    execution_time: "capo_glue.types.execution_time.ExecutionTime"
    """<p>The amount of time (in seconds) that the run consumed resources.</p>"""
    recommended_ruleset: NotRequired[
        "capo_glue.types.data_quality_ruleset_string.DataQualityRulesetString"
    ]
    """<p>When a start rule recommendation run completes, it creates a recommended ruleset (a set of rules). This member has those rules in Data Quality Definition Language (DQDL) format.</p>"""
    created_ruleset_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the ruleset that was created by the run.</p>"""
    data_quality_security_configuration: NotRequired[
        "capo_glue.types.name_string.NameString"
    ]
    """<p>The name of the security configuration created with the data quality encryption option.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataQualityRuleRecommendationRunResponse) -> dict:
    out: dict = {}
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    if "data_source" in value:
        import capo_glue.types.data_source

        out["DataSource"] = capo_glue.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    if "role" in value:
        out["Role"] = value["role"]
    if "number_of_workers" in value:
        out["NumberOfWorkers"] = value["number_of_workers"]
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    if "status" in value:
        import capo_glue.types.task_status_type

        out["Status"] = capo_glue.types.task_status_type.serialize_aws_json_1_1(
            value["status"]
        )
    if "error_string" in value:
        out["ErrorString"] = value["error_string"]
    if "started_on" in value:
        import capo_glue.types.timestamp

        out["StartedOn"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_on"]
        )
    if "last_modified_on" in value:
        import capo_glue.types.timestamp

        out["LastModifiedOn"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_on"]
        )
    if "completed_on" in value:
        import capo_glue.types.timestamp

        out["CompletedOn"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["completed_on"]
        )
    out["ExecutionTime"] = value.get("execution_time", 0)
    if "recommended_ruleset" in value:
        out["RecommendedRuleset"] = value["recommended_ruleset"]
    if "created_ruleset_name" in value:
        out["CreatedRulesetName"] = value["created_ruleset_name"]
    if "data_quality_security_configuration" in value:
        out["DataQualitySecurityConfiguration"] = value[
            "data_quality_security_configuration"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataQualityRuleRecommendationRunResponse:
    out: GetDataQualityRuleRecommendationRunResponse = {}  # type: ignore[typeddict-item]
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    if "DataSource" in data:
        import capo_glue.types.data_source

        out["data_source"] = capo_glue.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    if "Role" in data:
        out["role"] = data["Role"]
    if "NumberOfWorkers" in data:
        out["number_of_workers"] = data["NumberOfWorkers"]
    if "Timeout" in data:
        out["timeout"] = data["Timeout"]
    if "Status" in data:
        import capo_glue.types.task_status_type

        out["status"] = capo_glue.types.task_status_type.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "ErrorString" in data:
        out["error_string"] = data["ErrorString"]
    if "StartedOn" in data:
        import capo_glue.types.timestamp

        out["started_on"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedOn"]
        )
    if "LastModifiedOn" in data:
        import capo_glue.types.timestamp

        out["last_modified_on"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["LastModifiedOn"]
        )
    if "CompletedOn" in data:
        import capo_glue.types.timestamp

        out["completed_on"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CompletedOn"]
        )
    if "ExecutionTime" in data:
        out["execution_time"] = data["ExecutionTime"]
    else:
        out["execution_time"] = 0
    if "RecommendedRuleset" in data:
        out["recommended_ruleset"] = data["RecommendedRuleset"]
    if "CreatedRulesetName" in data:
        out["created_ruleset_name"] = data["CreatedRulesetName"]
    if "DataQualitySecurityConfiguration" in data:
        out["data_quality_security_configuration"] = data[
            "DataQualitySecurityConfiguration"
        ]
    return out
