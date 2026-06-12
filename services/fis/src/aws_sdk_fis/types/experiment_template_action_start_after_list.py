"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateActionStartAfterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_template_action_start_after

ExperimentTemplateActionStartAfterList: TypeAlias = list[
    "aws_sdk_fis.types.experiment_template_action_start_after.ExperimentTemplateActionStartAfter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTemplateActionStartAfterList) -> list:
    return list(value)


def deserialize_json(data: list) -> ExperimentTemplateActionStartAfterList:
    return list(data)
