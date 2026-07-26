"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityRulesetEvaluationRunDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_source
    import capo_glue.types.hash_string
    import capo_glue.types.task_status_type
    import capo_glue.types.timestamp


class DataQualityRulesetEvaluationRunDescription(TypedDict, closed=True):
    run_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The unique run identifier associated with this run.</p>"""
    status: NotRequired["capo_glue.types.task_status_type.TaskStatusType"]
    """<p>The status for this run.</p>"""
    started_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The date and time when the run started.</p>"""
    data_source: NotRequired["capo_glue.types.data_source.DataSource"]
    """<p>The data source (an Glue table) associated with the run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityRulesetEvaluationRunDescription) -> dict:
    out: dict = {}
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    if "status" in value:
        import capo_glue.types.task_status_type

        out["Status"] = capo_glue.types.task_status_type.serialize_aws_json_1_1(
            value["status"]
        )
    if "started_on" in value:
        import capo_glue.types.timestamp

        out["StartedOn"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_on"]
        )
    if "data_source" in value:
        import capo_glue.types.data_source

        out["DataSource"] = capo_glue.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityRulesetEvaluationRunDescription:
    out: DataQualityRulesetEvaluationRunDescription = {}  # type: ignore[typeddict-item]
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    if "Status" in data:
        import capo_glue.types.task_status_type

        out["status"] = capo_glue.types.task_status_type.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "StartedOn" in data:
        import capo_glue.types.timestamp

        out["started_on"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedOn"]
        )
    if "DataSource" in data:
        import capo_glue.types.data_source

        out["data_source"] = capo_glue.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    return out
