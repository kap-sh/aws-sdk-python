"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTargetFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.experiment_target_filter

ExperimentTargetFilterList: TypeAlias = list[
    "capo_fis.types.experiment_target_filter.ExperimentTargetFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTargetFilterList) -> list:
    import capo_fis.types.experiment_target_filter

    out: list = []
    for item in value:
        out.append(capo_fis.types.experiment_target_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExperimentTargetFilterList:
    import capo_fis.types.experiment_target_filter

    out: ExperimentTargetFilterList = []
    for item in data:
        out.append(capo_fis.types.experiment_target_filter.deserialize_json(item))
    return out
