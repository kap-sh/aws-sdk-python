"""Generated from Smithy shape ``com.amazonaws.fis#CreateExperimentTemplateStopConditionInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.create_experiment_template_stop_condition_input

CreateExperimentTemplateStopConditionInputList: TypeAlias = list[
    "capo_fis.types.create_experiment_template_stop_condition_input.CreateExperimentTemplateStopConditionInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateExperimentTemplateStopConditionInputList) -> list:
    import capo_fis.types.create_experiment_template_stop_condition_input

    out: list = []
    for item in value:
        out.append(
            capo_fis.types.create_experiment_template_stop_condition_input.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CreateExperimentTemplateStopConditionInputList:
    import capo_fis.types.create_experiment_template_stop_condition_input

    out: CreateExperimentTemplateStopConditionInputList = []
    for item in data:
        out.append(
            capo_fis.types.create_experiment_template_stop_condition_input.deserialize_json(
                item
            )
        )
    return out
