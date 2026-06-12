"""Generated from Smithy shape ``com.amazonaws.frauddetector#BatchGetVariableResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.batch_get_variable_error_list
    import aws_sdk_frauddetector.types.variable_list


class BatchGetVariableResult(TypedDict):
    variables: NotRequired["aws_sdk_frauddetector.types.variable_list.VariableList"]
    """<p>The returned variables.</p>"""
    errors: NotRequired[
        "aws_sdk_frauddetector.types.batch_get_variable_error_list.BatchGetVariableErrorList"
    ]
    """<p>The errors from the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetVariableResult) -> dict:
    out: dict = {}
    if "variables" in value:
        import aws_sdk_frauddetector.types.variable_list

        out["variables"] = (
            aws_sdk_frauddetector.types.variable_list.serialize_aws_json_1_1(
                value["variables"]
            )
        )
    if "errors" in value:
        import aws_sdk_frauddetector.types.batch_get_variable_error_list

        out["errors"] = (
            aws_sdk_frauddetector.types.batch_get_variable_error_list.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetVariableResult:
    out: BatchGetVariableResult = {}  # type: ignore[typeddict-item]
    if "variables" in data:
        import aws_sdk_frauddetector.types.variable_list

        out["variables"] = (
            aws_sdk_frauddetector.types.variable_list.deserialize_aws_json_1_1(
                data["variables"]
            )
        )
    if "errors" in data:
        import aws_sdk_frauddetector.types.batch_get_variable_error_list

        out["errors"] = (
            aws_sdk_frauddetector.types.batch_get_variable_error_list.deserialize_aws_json_1_1(
                data["errors"]
            )
        )
    return out
