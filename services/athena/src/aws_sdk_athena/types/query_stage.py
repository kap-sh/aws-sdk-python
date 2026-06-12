"""Generated from Smithy shape ``com.amazonaws.athena#QueryStage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.long
    import aws_sdk_athena.types.query_stage_plan_node
    import aws_sdk_athena.types.query_stages
    import aws_sdk_athena.types.string


class QueryStage(TypedDict):
    stage_id: NotRequired["aws_sdk_athena.types.long.Long"]
    """<p>The identifier for a stage.</p>"""
    state: NotRequired["aws_sdk_athena.types.string.String"]
    """<p>State of the stage after query execution.</p>"""
    output_bytes: NotRequired["aws_sdk_athena.types.long.Long"]
    """<p>The number of bytes output from the stage after execution.</p>"""
    output_rows: NotRequired["aws_sdk_athena.types.long.Long"]
    """<p>The number of rows output from the stage after execution.</p>"""
    input_bytes: NotRequired["aws_sdk_athena.types.long.Long"]
    """<p>The number of bytes input into the stage for execution.</p>"""
    input_rows: NotRequired["aws_sdk_athena.types.long.Long"]
    """<p>The number of rows input into the stage for execution.</p>"""
    execution_time: NotRequired["aws_sdk_athena.types.long.Long"]
    """<p>Time taken to execute this stage.</p>"""
    query_stage_plan: NotRequired[
        "aws_sdk_athena.types.query_stage_plan_node.QueryStagePlanNode"
    ]
    """<p>Stage plan information such as name, identifier, sub plans, and source stages.</p>"""
    sub_stages: NotRequired["aws_sdk_athena.types.query_stages.QueryStages"]
    """<p>List of sub query stages that form this stage execution plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryStage) -> dict:
    out: dict = {}
    if "stage_id" in value:
        out["StageId"] = value["stage_id"]
    if "state" in value:
        out["State"] = value["state"]
    if "output_bytes" in value:
        out["OutputBytes"] = value["output_bytes"]
    if "output_rows" in value:
        out["OutputRows"] = value["output_rows"]
    if "input_bytes" in value:
        out["InputBytes"] = value["input_bytes"]
    if "input_rows" in value:
        out["InputRows"] = value["input_rows"]
    if "execution_time" in value:
        out["ExecutionTime"] = value["execution_time"]
    if "query_stage_plan" in value:
        import aws_sdk_athena.types.query_stage_plan_node

        out["QueryStagePlan"] = (
            aws_sdk_athena.types.query_stage_plan_node.serialize_aws_json_1_1(
                value["query_stage_plan"]
            )
        )
    if "sub_stages" in value:
        import aws_sdk_athena.types.query_stages

        out["SubStages"] = aws_sdk_athena.types.query_stages.serialize_aws_json_1_1(
            value["sub_stages"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryStage:
    out: QueryStage = {}  # type: ignore[typeddict-item]
    if "StageId" in data:
        out["stage_id"] = data["StageId"]
    if "State" in data:
        out["state"] = data["State"]
    if "OutputBytes" in data:
        out["output_bytes"] = data["OutputBytes"]
    if "OutputRows" in data:
        out["output_rows"] = data["OutputRows"]
    if "InputBytes" in data:
        out["input_bytes"] = data["InputBytes"]
    if "InputRows" in data:
        out["input_rows"] = data["InputRows"]
    if "ExecutionTime" in data:
        out["execution_time"] = data["ExecutionTime"]
    if "QueryStagePlan" in data:
        import aws_sdk_athena.types.query_stage_plan_node

        out["query_stage_plan"] = (
            aws_sdk_athena.types.query_stage_plan_node.deserialize_aws_json_1_1(
                data["QueryStagePlan"]
            )
        )
    if "SubStages" in data:
        import aws_sdk_athena.types.query_stages

        out["sub_stages"] = aws_sdk_athena.types.query_stages.deserialize_aws_json_1_1(
            data["SubStages"]
        )
    return out
