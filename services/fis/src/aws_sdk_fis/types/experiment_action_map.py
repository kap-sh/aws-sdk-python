"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentActionMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_action
    import aws_sdk_fis.types.experiment_action_name

ExperimentActionMap: TypeAlias = dict[
    "aws_sdk_fis.types.experiment_action_name.ExperimentActionName",
    "aws_sdk_fis.types.experiment_action.ExperimentAction",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExperimentActionMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_fis.types.experiment_action

        out[key] = aws_sdk_fis.types.experiment_action.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ExperimentActionMap:
    out: ExperimentActionMap = {}
    for key, value in data.items():
        import aws_sdk_fis.types.experiment_action

        out[key] = aws_sdk_fis.types.experiment_action.deserialize_json(value)
    return out
