"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentActionParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.experiment_action_parameter
    import capo_fis.types.experiment_action_parameter_name

ExperimentActionParameterMap: TypeAlias = dict[
    "capo_fis.types.experiment_action_parameter_name.ExperimentActionParameterName",
    "capo_fis.types.experiment_action_parameter.ExperimentActionParameter",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExperimentActionParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ExperimentActionParameterMap:
    out: ExperimentActionParameterMap = {}
    for key, value in data.items():
        out[key] = value
    return out
