"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateTargetFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.experiment_template_target_filter

ExperimentTemplateTargetFilterList: TypeAlias = list[
    "capo_fis.types.experiment_template_target_filter.ExperimentTemplateTargetFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTemplateTargetFilterList) -> list:
    import capo_fis.types.experiment_template_target_filter

    out: list = []
    for item in value:
        out.append(
            capo_fis.types.experiment_template_target_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ExperimentTemplateTargetFilterList:
    import capo_fis.types.experiment_template_target_filter

    out: ExperimentTemplateTargetFilterList = []
    for item in data:
        out.append(
            capo_fis.types.experiment_template_target_filter.deserialize_json(item)
        )
    return out
