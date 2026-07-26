"""Generated from Smithy shape ``com.amazonaws.deadline#TaskParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.string
    import capo_deadline.types.task_parameter_value

TaskParameters: TypeAlias = dict[
    "capo_deadline.types.string.String",
    "capo_deadline.types.task_parameter_value.TaskParameterValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TaskParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_deadline.types.task_parameter_value

        out[key] = capo_deadline.types.task_parameter_value.serialize_json(value)
    return out


def deserialize_json(data: dict) -> TaskParameters:
    out: TaskParameters = {}
    for key, value in data.items():
        import capo_deadline.types.task_parameter_value

        out[key] = capo_deadline.types.task_parameter_value.deserialize_json(value)
    return out
