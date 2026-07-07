"""Generated from Smithy shape ``com.amazonaws.bedrock#TeacherModelConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.teacher_model_identifier


class TeacherModelConfig(TypedDict, closed=True):
    teacher_model_identifier: (
        "aws_sdk_bedrock.types.teacher_model_identifier.TeacherModelIdentifier"
    )
    """<p>The identifier of the teacher model.</p>"""
    max_response_length_for_inference: NotRequired["int"]
    """<p>The maximum number of tokens requested when the customization job invokes the teacher model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TeacherModelConfig) -> dict:
    out: dict = {}
    out["teacherModelIdentifier"] = value["teacher_model_identifier"]
    if "max_response_length_for_inference" in value:
        out["maxResponseLengthForInference"] = value[
            "max_response_length_for_inference"
        ]
    return out


def deserialize_json(data: dict) -> TeacherModelConfig:
    out: TeacherModelConfig = {}  # type: ignore[typeddict-item]
    if "teacherModelIdentifier" in data:
        out["teacher_model_identifier"] = data["teacherModelIdentifier"]
    else:
        raise DeserializationError(
            "TeacherModelConfig.teacher_model_identifier required"
        )
    if "maxResponseLengthForInference" in data:
        out["max_response_length_for_inference"] = data["maxResponseLengthForInference"]
    return out
