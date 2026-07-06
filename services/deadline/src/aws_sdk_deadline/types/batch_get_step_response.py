"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetStepResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_step_errors
    import aws_sdk_deadline.types.batch_get_step_items


class BatchGetStepResponse(TypedDict, closed=True):
    steps: "aws_sdk_deadline.types.batch_get_step_items.BatchGetStepItems"
    """<p>A list of steps that were successfully retrieved.</p>"""
    errors: "aws_sdk_deadline.types.batch_get_step_errors.BatchGetStepErrors"
    """<p>A list of errors for steps that could not be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetStepResponse) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.batch_get_step_items

    out["steps"] = aws_sdk_deadline.types.batch_get_step_items.serialize_json(
        value["steps"]
    )
    import aws_sdk_deadline.types.batch_get_step_errors

    out["errors"] = aws_sdk_deadline.types.batch_get_step_errors.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetStepResponse:
    out: BatchGetStepResponse = {}  # type: ignore[typeddict-item]
    if "steps" in data:
        import aws_sdk_deadline.types.batch_get_step_items

        out["steps"] = aws_sdk_deadline.types.batch_get_step_items.deserialize_json(
            data["steps"]
        )
    else:
        raise DeserializationError("BatchGetStepResponse.steps required")
    if "errors" in data:
        import aws_sdk_deadline.types.batch_get_step_errors

        out["errors"] = aws_sdk_deadline.types.batch_get_step_errors.deserialize_json(
            data["errors"]
        )
    else:
        raise DeserializationError("BatchGetStepResponse.errors required")
    return out
