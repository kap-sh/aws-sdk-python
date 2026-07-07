"""Generated from Smithy shape ``com.amazonaws.deadline#StepParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.step_parameter_chunks
    import aws_sdk_deadline.types.step_parameter_name
    import aws_sdk_deadline.types.step_parameter_type


class StepParameter(TypedDict, closed=True):
    name: "aws_sdk_deadline.types.step_parameter_name.StepParameterName"
    """<p>The name of the parameter.</p>"""
    type: "aws_sdk_deadline.types.step_parameter_type.StepParameterType"
    """<p>The data type of the parameter.</p>"""
    chunks: NotRequired[
        "aws_sdk_deadline.types.step_parameter_chunks.StepParameterChunks"
    ]
    """<p>The configuration for task chunking.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepParameter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_deadline.types.step_parameter_type

    out["type"] = aws_sdk_deadline.types.step_parameter_type.serialize_json(
        value["type"]
    )
    if "chunks" in value:
        import aws_sdk_deadline.types.step_parameter_chunks

        out["chunks"] = aws_sdk_deadline.types.step_parameter_chunks.serialize_json(
            value["chunks"]
        )
    return out


def deserialize_json(data: dict) -> StepParameter:
    out: StepParameter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StepParameter.name required")
    if "type" in data:
        import aws_sdk_deadline.types.step_parameter_type

        out["type"] = aws_sdk_deadline.types.step_parameter_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("StepParameter.type required")
    if "chunks" in data:
        import aws_sdk_deadline.types.step_parameter_chunks

        out["chunks"] = aws_sdk_deadline.types.step_parameter_chunks.deserialize_json(
            data["chunks"]
        )
    return out
