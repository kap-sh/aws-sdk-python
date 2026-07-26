"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentActionMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.experiment_action
    import capo_fis.types.experiment_action_name

ExperimentActionMap: TypeAlias = dict[
    "capo_fis.types.experiment_action_name.ExperimentActionName",
    "capo_fis.types.experiment_action.ExperimentAction",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExperimentActionMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_fis.types.experiment_action

        out[key] = capo_fis.types.experiment_action.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ExperimentActionMap:
    out: ExperimentActionMap = {}
    for key, value in data.items():
        import capo_fis.types.experiment_action

        out[key] = capo_fis.types.experiment_action.deserialize_json(value)
    return out
