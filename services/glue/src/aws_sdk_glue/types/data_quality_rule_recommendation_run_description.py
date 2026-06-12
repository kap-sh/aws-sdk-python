"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityRuleRecommendationRunDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_source
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.task_status_type
    import aws_sdk_glue.types.timestamp


class DataQualityRuleRecommendationRunDescription(TypedDict):
    run_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The unique run identifier associated with this run.</p>"""
    status: NotRequired["aws_sdk_glue.types.task_status_type.TaskStatusType"]
    """<p>The status for this run.</p>"""
    started_on: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The date and time when this run started.</p>"""
    data_source: NotRequired["aws_sdk_glue.types.data_source.DataSource"]
    """<p>The data source (Glue table) associated with the recommendation run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityRuleRecommendationRunDescription) -> dict:
    out: dict = {}
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    if "status" in value:
        import aws_sdk_glue.types.task_status_type

        out["Status"] = aws_sdk_glue.types.task_status_type.serialize_aws_json_1_1(
            value["status"]
        )
    if "started_on" in value:
        import aws_sdk_glue.types.timestamp

        out["StartedOn"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_on"]
        )
    if "data_source" in value:
        import aws_sdk_glue.types.data_source

        out["DataSource"] = aws_sdk_glue.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityRuleRecommendationRunDescription:
    out: DataQualityRuleRecommendationRunDescription = {}  # type: ignore[typeddict-item]
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    if "Status" in data:
        import aws_sdk_glue.types.task_status_type

        out["status"] = aws_sdk_glue.types.task_status_type.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "StartedOn" in data:
        import aws_sdk_glue.types.timestamp

        out["started_on"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedOn"]
        )
    if "DataSource" in data:
        import aws_sdk_glue.types.data_source

        out["data_source"] = aws_sdk_glue.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    return out
