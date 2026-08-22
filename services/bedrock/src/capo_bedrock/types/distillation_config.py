"""Generated from Smithy shape ``com.amazonaws.bedrock#DistillationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.teacher_model_config


class DistillationConfig(TypedDict, closed=True):
    teacher_model_config: "capo_bedrock.types.teacher_model_config.TeacherModelConfig"
    """<p>The teacher model configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DistillationConfig) -> dict:
    out: dict = {}
    import capo_bedrock.types.teacher_model_config

    out["teacherModelConfig"] = capo_bedrock.types.teacher_model_config.serialize_json(
        value["teacher_model_config"]
    )
    return out


def deserialize_json(data: dict) -> DistillationConfig:
    out: DistillationConfig = {}  # type: ignore[typeddict-item]
    if data.get("teacherModelConfig") is not None:
        import capo_bedrock.types.teacher_model_config

        out["teacher_model_config"] = (
            capo_bedrock.types.teacher_model_config.deserialize_json(
                data["teacherModelConfig"]
            )
        )
    else:
        raise DeserializationError("DistillationConfig.teacher_model_config required")
    return out
