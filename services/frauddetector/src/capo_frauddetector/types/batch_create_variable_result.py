"""Generated from Smithy shape ``com.amazonaws.frauddetector#BatchCreateVariableResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.batch_create_variable_error_list


class BatchCreateVariableResult(TypedDict, closed=True):
    errors: NotRequired[
        "capo_frauddetector.types.batch_create_variable_error_list.BatchCreateVariableErrorList"
    ]
    """<p>Provides the errors for the <code>BatchCreateVariable</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchCreateVariableResult) -> dict:
    out: dict = {}
    if "errors" in value:
        import capo_frauddetector.types.batch_create_variable_error_list

        out["errors"] = (
            capo_frauddetector.types.batch_create_variable_error_list.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchCreateVariableResult:
    out: BatchCreateVariableResult = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import capo_frauddetector.types.batch_create_variable_error_list

        out["errors"] = (
            capo_frauddetector.types.batch_create_variable_error_list.deserialize_aws_json_1_1(
                data["errors"]
            )
        )
    return out
