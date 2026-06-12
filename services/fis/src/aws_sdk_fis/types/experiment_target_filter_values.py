"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTargetFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_target_filter_value

ExperimentTargetFilterValues: TypeAlias = list[
    "aws_sdk_fis.types.experiment_target_filter_value.ExperimentTargetFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTargetFilterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> ExperimentTargetFilterValues:
    return list(data)
