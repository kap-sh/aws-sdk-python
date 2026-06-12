"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_aggregated_metrics
    import aws_sdk_glue.types.data_quality_analyzer_results
    import aws_sdk_glue.types.data_quality_observations
    import aws_sdk_glue.types.data_quality_rule_results
    import aws_sdk_glue.types.data_source
    import aws_sdk_glue.types.generic_bounded_double
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.timestamp


class DataQualityResult(TypedDict):
    result_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>A unique result ID for the data quality result.</p>"""
    profile_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The Profile ID for the data quality result.</p>"""
    score: NotRequired["aws_sdk_glue.types.generic_bounded_double.GenericBoundedDouble"]
    """<p>An aggregate data quality score. Represents the ratio of rules that passed to the total number of rules.</p>"""
    data_source: NotRequired["aws_sdk_glue.types.data_source.DataSource"]
    """<p>The table associated with the data quality result, if any.</p>"""
    ruleset_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the ruleset associated with the data quality result.</p>"""
    evaluation_context: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>In the context of a job in Glue Studio, each node in the canvas is typically assigned some sort of name and data quality nodes will have names. In the case of multiple nodes, the <code>evaluationContext</code> can differentiate the nodes.</p>"""
    started_on: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The date and time when this data quality run started.</p>"""
    completed_on: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The date and time when this data quality run completed.</p>"""
    job_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The job name associated with the data quality result, if any.</p>"""
    job_run_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The job run ID associated with the data quality result, if any.</p>"""
    ruleset_evaluation_run_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The unique run ID for the ruleset evaluation for this data quality result.</p>"""
    rule_results: NotRequired[
        "aws_sdk_glue.types.data_quality_rule_results.DataQualityRuleResults"
    ]
    """<p>A list of <code>DataQualityRuleResult</code> objects representing the results for each rule. </p>"""
    analyzer_results: NotRequired[
        "aws_sdk_glue.types.data_quality_analyzer_results.DataQualityAnalyzerResults"
    ]
    """<p>A list of <code>DataQualityAnalyzerResult</code> objects representing the results for each analyzer. </p>"""
    observations: NotRequired[
        "aws_sdk_glue.types.data_quality_observations.DataQualityObservations"
    ]
    """<p>A list of <code>DataQualityObservation</code> objects representing the observations generated after evaluating the rules and analyzers. </p>"""
    aggregated_metrics: NotRequired[
        "aws_sdk_glue.types.data_quality_aggregated_metrics.DataQualityAggregatedMetrics"
    ]
    """<p> A summary of <code>DataQualityAggregatedMetrics</code> objects showing the total counts of processed rows and rules, including their pass/fail statistics based on row-level results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityResult) -> dict:
    out: dict = {}
    if "result_id" in value:
        out["ResultId"] = value["result_id"]
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    if "score" in value:
        out["Score"] = value["score"]
    if "data_source" in value:
        import aws_sdk_glue.types.data_source

        out["DataSource"] = aws_sdk_glue.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    if "ruleset_name" in value:
        out["RulesetName"] = value["ruleset_name"]
    if "evaluation_context" in value:
        out["EvaluationContext"] = value["evaluation_context"]
    if "started_on" in value:
        import aws_sdk_glue.types.timestamp

        out["StartedOn"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_on"]
        )
    if "completed_on" in value:
        import aws_sdk_glue.types.timestamp

        out["CompletedOn"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["completed_on"]
        )
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_run_id" in value:
        out["JobRunId"] = value["job_run_id"]
    if "ruleset_evaluation_run_id" in value:
        out["RulesetEvaluationRunId"] = value["ruleset_evaluation_run_id"]
    if "rule_results" in value:
        import aws_sdk_glue.types.data_quality_rule_results

        out["RuleResults"] = (
            aws_sdk_glue.types.data_quality_rule_results.serialize_aws_json_1_1(
                value["rule_results"]
            )
        )
    if "analyzer_results" in value:
        import aws_sdk_glue.types.data_quality_analyzer_results

        out["AnalyzerResults"] = (
            aws_sdk_glue.types.data_quality_analyzer_results.serialize_aws_json_1_1(
                value["analyzer_results"]
            )
        )
    if "observations" in value:
        import aws_sdk_glue.types.data_quality_observations

        out["Observations"] = (
            aws_sdk_glue.types.data_quality_observations.serialize_aws_json_1_1(
                value["observations"]
            )
        )
    if "aggregated_metrics" in value:
        import aws_sdk_glue.types.data_quality_aggregated_metrics

        out["AggregatedMetrics"] = (
            aws_sdk_glue.types.data_quality_aggregated_metrics.serialize_aws_json_1_1(
                value["aggregated_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityResult:
    out: DataQualityResult = {}  # type: ignore[typeddict-item]
    if "ResultId" in data:
        out["result_id"] = data["ResultId"]
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    if "Score" in data:
        out["score"] = data["Score"]
    if "DataSource" in data:
        import aws_sdk_glue.types.data_source

        out["data_source"] = aws_sdk_glue.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    if "RulesetName" in data:
        out["ruleset_name"] = data["RulesetName"]
    if "EvaluationContext" in data:
        out["evaluation_context"] = data["EvaluationContext"]
    if "StartedOn" in data:
        import aws_sdk_glue.types.timestamp

        out["started_on"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedOn"]
        )
    if "CompletedOn" in data:
        import aws_sdk_glue.types.timestamp

        out["completed_on"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CompletedOn"]
        )
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobRunId" in data:
        out["job_run_id"] = data["JobRunId"]
    if "RulesetEvaluationRunId" in data:
        out["ruleset_evaluation_run_id"] = data["RulesetEvaluationRunId"]
    if "RuleResults" in data:
        import aws_sdk_glue.types.data_quality_rule_results

        out["rule_results"] = (
            aws_sdk_glue.types.data_quality_rule_results.deserialize_aws_json_1_1(
                data["RuleResults"]
            )
        )
    if "AnalyzerResults" in data:
        import aws_sdk_glue.types.data_quality_analyzer_results

        out["analyzer_results"] = (
            aws_sdk_glue.types.data_quality_analyzer_results.deserialize_aws_json_1_1(
                data["AnalyzerResults"]
            )
        )
    if "Observations" in data:
        import aws_sdk_glue.types.data_quality_observations

        out["observations"] = (
            aws_sdk_glue.types.data_quality_observations.deserialize_aws_json_1_1(
                data["Observations"]
            )
        )
    if "AggregatedMetrics" in data:
        import aws_sdk_glue.types.data_quality_aggregated_metrics

        out["aggregated_metrics"] = (
            aws_sdk_glue.types.data_quality_aggregated_metrics.deserialize_aws_json_1_1(
                data["AggregatedMetrics"]
            )
        )
    return out
