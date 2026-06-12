"""Generated from Smithy shape ``com.amazonaws.glue#StartDataQualityRulesetEvaluationRunRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_evaluation_run_additional_run_options
    import aws_sdk_glue.types.data_source
    import aws_sdk_glue.types.data_source_map
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.nullable_integer
    import aws_sdk_glue.types.role_string
    import aws_sdk_glue.types.ruleset_names
    import aws_sdk_glue.types.timeout


class StartDataQualityRulesetEvaluationRunRequest(TypedDict):
    data_source: "aws_sdk_glue.types.data_source.DataSource"
    """<p>The data source (Glue table) associated with this run.</p>"""
    role: "aws_sdk_glue.types.role_string.RoleString"
    """<p>An IAM role supplied to encrypt the results of the run.</p>"""
    number_of_workers: NotRequired[
        "aws_sdk_glue.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of <code>G.1X</code> workers to be used in the run. The default is 5.</p>"""
    timeout: NotRequired["aws_sdk_glue.types.timeout.Timeout"]
    """<p>The timeout for a run in minutes. This is the maximum time that a run can consume resources before it is terminated and enters <code>TIMEOUT</code> status. The default is 2,880 minutes (48 hours).</p>"""
    client_token: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>Used for idempotency and is recommended to be set to a random ID (such as a UUID) to avoid creating or starting multiple instances of the same resource.</p>"""
    additional_run_options: NotRequired[
        "aws_sdk_glue.types.data_quality_evaluation_run_additional_run_options.DataQualityEvaluationRunAdditionalRunOptions"
    ]
    """<p>Additional run options you can specify for an evaluation run.</p>"""
    ruleset_names: "aws_sdk_glue.types.ruleset_names.RulesetNames"
    """<p>A list of ruleset names.</p>"""
    additional_data_sources: NotRequired[
        "aws_sdk_glue.types.data_source_map.DataSourceMap"
    ]
    """<p>A map of reference strings to additional data sources you can specify for an evaluation run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDataQualityRulesetEvaluationRunRequest) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.data_source

    out["DataSource"] = aws_sdk_glue.types.data_source.serialize_aws_json_1_1(
        value["data_source"]
    )
    out["Role"] = value["role"]
    if "number_of_workers" in value:
        out["NumberOfWorkers"] = value["number_of_workers"]
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "additional_run_options" in value:
        import aws_sdk_glue.types.data_quality_evaluation_run_additional_run_options

        out["AdditionalRunOptions"] = (
            aws_sdk_glue.types.data_quality_evaluation_run_additional_run_options.serialize_aws_json_1_1(
                value["additional_run_options"]
            )
        )
    import aws_sdk_glue.types.ruleset_names

    out["RulesetNames"] = aws_sdk_glue.types.ruleset_names.serialize_aws_json_1_1(
        value["ruleset_names"]
    )
    if "additional_data_sources" in value:
        import aws_sdk_glue.types.data_source_map

        out["AdditionalDataSources"] = (
            aws_sdk_glue.types.data_source_map.serialize_aws_json_1_1(
                value["additional_data_sources"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartDataQualityRulesetEvaluationRunRequest:
    out: StartDataQualityRulesetEvaluationRunRequest = {}  # type: ignore[typeddict-item]
    if "DataSource" in data:
        import aws_sdk_glue.types.data_source

        out["data_source"] = aws_sdk_glue.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    else:
        raise DeserializationError(
            "StartDataQualityRulesetEvaluationRunRequest.data_source required"
        )
    if "Role" in data:
        out["role"] = data["Role"]
    else:
        raise DeserializationError(
            "StartDataQualityRulesetEvaluationRunRequest.role required"
        )
    if "NumberOfWorkers" in data:
        out["number_of_workers"] = data["NumberOfWorkers"]
    if "Timeout" in data:
        out["timeout"] = data["Timeout"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "AdditionalRunOptions" in data:
        import aws_sdk_glue.types.data_quality_evaluation_run_additional_run_options

        out["additional_run_options"] = (
            aws_sdk_glue.types.data_quality_evaluation_run_additional_run_options.deserialize_aws_json_1_1(
                data["AdditionalRunOptions"]
            )
        )
    if "RulesetNames" in data:
        import aws_sdk_glue.types.ruleset_names

        out["ruleset_names"] = (
            aws_sdk_glue.types.ruleset_names.deserialize_aws_json_1_1(
                data["RulesetNames"]
            )
        )
    else:
        raise DeserializationError(
            "StartDataQualityRulesetEvaluationRunRequest.ruleset_names required"
        )
    if "AdditionalDataSources" in data:
        import aws_sdk_glue.types.data_source_map

        out["additional_data_sources"] = (
            aws_sdk_glue.types.data_source_map.deserialize_aws_json_1_1(
                data["AdditionalDataSources"]
            )
        )
    return out
