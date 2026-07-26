"""Generated from Smithy shape ``com.amazonaws.glue#GetDataQualityRulesetEvaluationRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_evaluation_run_additional_run_options
    import capo_glue.types.data_quality_result_id_list
    import capo_glue.types.data_source
    import capo_glue.types.data_source_map
    import capo_glue.types.execution_time
    import capo_glue.types.generic_string
    import capo_glue.types.hash_string
    import capo_glue.types.nullable_integer
    import capo_glue.types.role_string
    import capo_glue.types.ruleset_names
    import capo_glue.types.task_status_type
    import capo_glue.types.timeout
    import capo_glue.types.timestamp


class GetDataQualityRulesetEvaluationRunResponse(TypedDict, closed=True):
    run_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The unique run identifier associated with this run.</p>"""
    data_source: NotRequired["capo_glue.types.data_source.DataSource"]
    """<p>The data source (an Glue table) associated with this evaluation run.</p>"""
    role: NotRequired["capo_glue.types.role_string.RoleString"]
    """<p>An IAM role supplied to encrypt the results of the run.</p>"""
    number_of_workers: NotRequired["capo_glue.types.nullable_integer.NullableInteger"]
    """<p>The number of <code>G.1X</code> workers to be used in the run. The default is 5.</p>"""
    timeout: NotRequired["capo_glue.types.timeout.Timeout"]
    """<p>The timeout for a run in minutes. This is the maximum time that a run can consume resources before it is terminated and enters <code>TIMEOUT</code> status. The default is 2,880 minutes (48 hours).</p>"""
    additional_run_options: NotRequired[
        "capo_glue.types.data_quality_evaluation_run_additional_run_options.DataQualityEvaluationRunAdditionalRunOptions"
    ]
    """<p>Additional run options you can specify for an evaluation run.</p>"""
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
    ruleset_names: NotRequired["capo_glue.types.ruleset_names.RulesetNames"]
    """<p>A list of ruleset names for the run. Currently, this parameter takes only one Ruleset name.</p>"""
    result_ids: NotRequired[
        "capo_glue.types.data_quality_result_id_list.DataQualityResultIdList"
    ]
    """<p>A list of result IDs for the data quality results for the run.</p>"""
    additional_data_sources: NotRequired[
        "capo_glue.types.data_source_map.DataSourceMap"
    ]
    """<p>A map of reference strings to additional data sources you can specify for an evaluation run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataQualityRulesetEvaluationRunResponse) -> dict:
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
    if "additional_run_options" in value:
        import capo_glue.types.data_quality_evaluation_run_additional_run_options

        out["AdditionalRunOptions"] = (
            capo_glue.types.data_quality_evaluation_run_additional_run_options.serialize_aws_json_1_1(
                value["additional_run_options"]
            )
        )
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
    if "ruleset_names" in value:
        import capo_glue.types.ruleset_names

        out["RulesetNames"] = capo_glue.types.ruleset_names.serialize_aws_json_1_1(
            value["ruleset_names"]
        )
    if "result_ids" in value:
        import capo_glue.types.data_quality_result_id_list

        out["ResultIds"] = (
            capo_glue.types.data_quality_result_id_list.serialize_aws_json_1_1(
                value["result_ids"]
            )
        )
    if "additional_data_sources" in value:
        import capo_glue.types.data_source_map

        out["AdditionalDataSources"] = (
            capo_glue.types.data_source_map.serialize_aws_json_1_1(
                value["additional_data_sources"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataQualityRulesetEvaluationRunResponse:
    out: GetDataQualityRulesetEvaluationRunResponse = {}  # type: ignore[typeddict-item]
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
    if "AdditionalRunOptions" in data:
        import capo_glue.types.data_quality_evaluation_run_additional_run_options

        out["additional_run_options"] = (
            capo_glue.types.data_quality_evaluation_run_additional_run_options.deserialize_aws_json_1_1(
                data["AdditionalRunOptions"]
            )
        )
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
    if "RulesetNames" in data:
        import capo_glue.types.ruleset_names

        out["ruleset_names"] = capo_glue.types.ruleset_names.deserialize_aws_json_1_1(
            data["RulesetNames"]
        )
    if "ResultIds" in data:
        import capo_glue.types.data_quality_result_id_list

        out["result_ids"] = (
            capo_glue.types.data_quality_result_id_list.deserialize_aws_json_1_1(
                data["ResultIds"]
            )
        )
    if "AdditionalDataSources" in data:
        import capo_glue.types.data_source_map

        out["additional_data_sources"] = (
            capo_glue.types.data_source_map.deserialize_aws_json_1_1(
                data["AdditionalDataSources"]
            )
        )
    return out
