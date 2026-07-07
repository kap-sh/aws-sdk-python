"""Generated from Smithy shape ``com.amazonaws.glue#StatementOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.integer_value
    import aws_sdk_glue.types.orchestration_string_list
    import aws_sdk_glue.types.statement_output_data
    import aws_sdk_glue.types.statement_state


class StatementOutput(TypedDict, closed=True):
    data: NotRequired["aws_sdk_glue.types.statement_output_data.StatementOutputData"]
    """<p>The code execution output.</p>"""
    execution_count: "aws_sdk_glue.types.integer_value.IntegerValue"
    """<p>The execution count of the output.</p>"""
    status: NotRequired["aws_sdk_glue.types.statement_state.StatementState"]
    """<p>The status of the code execution output.</p>"""
    error_name: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>The name of the error in the output.</p>"""
    error_value: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>The error value of the output.</p>"""
    traceback: NotRequired[
        "aws_sdk_glue.types.orchestration_string_list.OrchestrationStringList"
    ]
    """<p>The traceback of the output.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatementOutput) -> dict:
    out: dict = {}
    if "data" in value:
        import aws_sdk_glue.types.statement_output_data

        out["Data"] = aws_sdk_glue.types.statement_output_data.serialize_aws_json_1_1(
            value["data"]
        )
    out["ExecutionCount"] = value.get("execution_count", 0)
    if "status" in value:
        import aws_sdk_glue.types.statement_state

        out["Status"] = aws_sdk_glue.types.statement_state.serialize_aws_json_1_1(
            value["status"]
        )
    if "error_name" in value:
        out["ErrorName"] = value["error_name"]
    if "error_value" in value:
        out["ErrorValue"] = value["error_value"]
    if "traceback" in value:
        import aws_sdk_glue.types.orchestration_string_list

        out["Traceback"] = (
            aws_sdk_glue.types.orchestration_string_list.serialize_aws_json_1_1(
                value["traceback"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StatementOutput:
    out: StatementOutput = {}  # type: ignore[typeddict-item]
    if "Data" in data:
        import aws_sdk_glue.types.statement_output_data

        out["data"] = aws_sdk_glue.types.statement_output_data.deserialize_aws_json_1_1(
            data["Data"]
        )
    if "ExecutionCount" in data:
        out["execution_count"] = data["ExecutionCount"]
    else:
        out["execution_count"] = 0
    if "Status" in data:
        import aws_sdk_glue.types.statement_state

        out["status"] = aws_sdk_glue.types.statement_state.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "ErrorName" in data:
        out["error_name"] = data["ErrorName"]
    if "ErrorValue" in data:
        out["error_value"] = data["ErrorValue"]
    if "Traceback" in data:
        import aws_sdk_glue.types.orchestration_string_list

        out["traceback"] = (
            aws_sdk_glue.types.orchestration_string_list.deserialize_aws_json_1_1(
                data["Traceback"]
            )
        )
    return out
