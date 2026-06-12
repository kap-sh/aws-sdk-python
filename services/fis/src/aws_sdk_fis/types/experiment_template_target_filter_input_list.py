"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateTargetFilterInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_template_target_input_filter

ExperimentTemplateTargetFilterInputList: TypeAlias = list[
    "aws_sdk_fis.types.experiment_template_target_input_filter.ExperimentTemplateTargetInputFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTemplateTargetFilterInputList) -> list:
    import aws_sdk_fis.types.experiment_template_target_input_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_fis.types.experiment_template_target_input_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ExperimentTemplateTargetFilterInputList:
    import aws_sdk_fis.types.experiment_template_target_input_filter

    out: ExperimentTemplateTargetFilterInputList = []
    for item in data:
        out.append(
            aws_sdk_fis.types.experiment_template_target_input_filter.deserialize_json(
                item
            )
        )
    return out
