"""Generated from Smithy shape ``com.amazonaws.fis#UpdateExperimentTemplateStopConditionInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.update_experiment_template_stop_condition_input

UpdateExperimentTemplateStopConditionInputList: TypeAlias = list[
    "aws_sdk_fis.types.update_experiment_template_stop_condition_input.UpdateExperimentTemplateStopConditionInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateExperimentTemplateStopConditionInputList) -> list:
    import aws_sdk_fis.types.update_experiment_template_stop_condition_input

    out: list = []
    for item in value:
        out.append(
            aws_sdk_fis.types.update_experiment_template_stop_condition_input.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> UpdateExperimentTemplateStopConditionInputList:
    import aws_sdk_fis.types.update_experiment_template_stop_condition_input

    out: UpdateExperimentTemplateStopConditionInputList = []
    for item in data:
        out.append(
            aws_sdk_fis.types.update_experiment_template_stop_condition_input.deserialize_json(
                item
            )
        )
    return out
