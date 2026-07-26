"""Generated from Smithy shape ``com.amazonaws.signin#Condition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_signin.types.condition_values

Condition: TypeAlias = dict["str", "capo_signin.types.condition_values.ConditionValues"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Condition) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_signin.types.condition_values

        out[key] = capo_signin.types.condition_values.serialize_json(value)
    return out


def deserialize_json(data: dict) -> Condition:
    out: Condition = {}
    for key, value in data.items():
        import capo_signin.types.condition_values

        out[key] = capo_signin.types.condition_values.deserialize_json(value)
    return out
