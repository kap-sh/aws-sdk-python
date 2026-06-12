"""Generated from Smithy shape ``com.amazonaws.deadline#StepParameterChunks``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.default_task_count
    import aws_sdk_deadline.types.range_constraint
    import aws_sdk_deadline.types.target_runtime_seconds


class StepParameterChunks(TypedDict):
    default_task_count: "aws_sdk_deadline.types.default_task_count.DefaultTaskCount"
    """<p>The number of tasks to combine into a single chunk by default.</p>"""
    target_runtime_seconds: NotRequired[
        "aws_sdk_deadline.types.target_runtime_seconds.TargetRuntimeSeconds"
    ]
    """<p>The number of seconds to aim for when forming chunks.</p>"""
    range_constraint: "aws_sdk_deadline.types.range_constraint.RangeConstraint"
    """<p>Specifies whether the chunked ranges must be contiguous or can have gaps between them.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepParameterChunks) -> dict:
    out: dict = {}
    out["defaultTaskCount"] = value["default_task_count"]
    if "target_runtime_seconds" in value:
        out["targetRuntimeSeconds"] = value["target_runtime_seconds"]
    import aws_sdk_deadline.types.range_constraint

    out["rangeConstraint"] = aws_sdk_deadline.types.range_constraint.serialize_json(
        value["range_constraint"]
    )
    return out


def deserialize_json(data: dict) -> StepParameterChunks:
    out: StepParameterChunks = {}  # type: ignore[typeddict-item]
    if "defaultTaskCount" in data:
        out["default_task_count"] = data["defaultTaskCount"]
    else:
        raise DeserializationError("StepParameterChunks.default_task_count required")
    if "targetRuntimeSeconds" in data:
        out["target_runtime_seconds"] = data["targetRuntimeSeconds"]
    if "rangeConstraint" in data:
        import aws_sdk_deadline.types.range_constraint

        out["range_constraint"] = (
            aws_sdk_deadline.types.range_constraint.deserialize_json(
                data["rangeConstraint"]
            )
        )
    else:
        raise DeserializationError("StepParameterChunks.range_constraint required")
    return out
