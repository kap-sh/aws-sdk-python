"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentFailureReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.environment_failure_reasons_list

EnvironmentFailureReasons: TypeAlias = dict[
    "str",
    "capo_datazone.types.environment_failure_reasons_list.EnvironmentFailureReasonsList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EnvironmentFailureReasons) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_datazone.types.environment_failure_reasons_list

        out[key] = capo_datazone.types.environment_failure_reasons_list.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> EnvironmentFailureReasons:
    out: EnvironmentFailureReasons = {}
    for key, value in data.items():
        import capo_datazone.types.environment_failure_reasons_list

        out[key] = (
            capo_datazone.types.environment_failure_reasons_list.deserialize_json(value)
        )
    return out
