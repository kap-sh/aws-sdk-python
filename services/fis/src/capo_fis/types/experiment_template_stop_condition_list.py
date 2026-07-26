"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateStopConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.experiment_template_stop_condition

ExperimentTemplateStopConditionList: TypeAlias = list[
    "capo_fis.types.experiment_template_stop_condition.ExperimentTemplateStopCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTemplateStopConditionList) -> list:
    import capo_fis.types.experiment_template_stop_condition

    out: list = []
    for item in value:
        out.append(
            capo_fis.types.experiment_template_stop_condition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ExperimentTemplateStopConditionList:
    import capo_fis.types.experiment_template_stop_condition

    out: ExperimentTemplateStopConditionList = []
    for item in data:
        out.append(
            capo_fis.types.experiment_template_stop_condition.deserialize_json(item)
        )
    return out
