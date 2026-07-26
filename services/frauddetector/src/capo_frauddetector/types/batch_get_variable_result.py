"""Generated from Smithy shape ``com.amazonaws.frauddetector#BatchGetVariableResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.batch_get_variable_error_list
    import capo_frauddetector.types.variable_list


class BatchGetVariableResult(TypedDict, closed=True):
    variables: NotRequired["capo_frauddetector.types.variable_list.VariableList"]
    """<p>The returned variables.</p>"""
    errors: NotRequired[
        "capo_frauddetector.types.batch_get_variable_error_list.BatchGetVariableErrorList"
    ]
    """<p>The errors from the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetVariableResult) -> dict:
    out: dict = {}
    if "variables" in value:
        import capo_frauddetector.types.variable_list

        out["variables"] = (
            capo_frauddetector.types.variable_list.serialize_aws_json_1_1(
                value["variables"]
            )
        )
    if "errors" in value:
        import capo_frauddetector.types.batch_get_variable_error_list

        out["errors"] = (
            capo_frauddetector.types.batch_get_variable_error_list.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetVariableResult:
    out: BatchGetVariableResult = {}  # type: ignore[typeddict-item]
    if "variables" in data:
        import capo_frauddetector.types.variable_list

        out["variables"] = (
            capo_frauddetector.types.variable_list.deserialize_aws_json_1_1(
                data["variables"]
            )
        )
    if "errors" in data:
        import capo_frauddetector.types.batch_get_variable_error_list

        out["errors"] = (
            capo_frauddetector.types.batch_get_variable_error_list.deserialize_aws_json_1_1(
                data["errors"]
            )
        )
    return out
