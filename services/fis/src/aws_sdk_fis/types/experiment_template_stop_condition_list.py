"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateStopConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_template_stop_condition

ExperimentTemplateStopConditionList: TypeAlias = list[
    "aws_sdk_fis.types.experiment_template_stop_condition.ExperimentTemplateStopCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTemplateStopConditionList) -> list:
    import aws_sdk_fis.types.experiment_template_stop_condition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_fis.types.experiment_template_stop_condition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ExperimentTemplateStopConditionList:
    import aws_sdk_fis.types.experiment_template_stop_condition

    out: ExperimentTemplateStopConditionList = []
    for item in data:
        out.append(
            aws_sdk_fis.types.experiment_template_stop_condition.deserialize_json(item)
        )
    return out
