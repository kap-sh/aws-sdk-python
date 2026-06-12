"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateTargetFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_template_target_filter_value

ExperimentTemplateTargetFilterValues: TypeAlias = list[
    "aws_sdk_fis.types.experiment_template_target_filter_value.ExperimentTemplateTargetFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTemplateTargetFilterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> ExperimentTemplateTargetFilterValues:
    return list(data)
