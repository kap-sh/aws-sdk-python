"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentStopConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_stop_condition

ExperimentStopConditionList: TypeAlias = list[
    "aws_sdk_fis.types.experiment_stop_condition.ExperimentStopCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentStopConditionList) -> list:
    import aws_sdk_fis.types.experiment_stop_condition

    out: list = []
    for item in value:
        out.append(aws_sdk_fis.types.experiment_stop_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExperimentStopConditionList:
    import aws_sdk_fis.types.experiment_stop_condition

    out: ExperimentStopConditionList = []
    for item in data:
        out.append(aws_sdk_fis.types.experiment_stop_condition.deserialize_json(item))
    return out
