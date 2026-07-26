"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateTargetFilterInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.experiment_template_target_input_filter

ExperimentTemplateTargetFilterInputList: TypeAlias = list[
    "capo_fis.types.experiment_template_target_input_filter.ExperimentTemplateTargetInputFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTemplateTargetFilterInputList) -> list:
    import capo_fis.types.experiment_template_target_input_filter

    out: list = []
    for item in value:
        out.append(
            capo_fis.types.experiment_template_target_input_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ExperimentTemplateTargetFilterInputList:
    import capo_fis.types.experiment_template_target_input_filter

    out: ExperimentTemplateTargetFilterInputList = []
    for item in data:
        out.append(
            capo_fis.types.experiment_template_target_input_filter.deserialize_json(
                item
            )
        )
    return out
