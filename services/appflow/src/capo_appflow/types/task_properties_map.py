"""Generated from Smithy shape ``com.amazonaws.appflow#TaskPropertiesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.operator_properties_keys
    import capo_appflow.types.property

TaskPropertiesMap: TypeAlias = dict[
    "capo_appflow.types.operator_properties_keys.OperatorPropertiesKeys",
    "capo_appflow.types.property.Property",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TaskPropertiesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_appflow.types.operator_properties_keys

        out[capo_appflow.types.operator_properties_keys.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> TaskPropertiesMap:
    out: TaskPropertiesMap = {}
    for key, value in data.items():
        import capo_appflow.types.operator_properties_keys

        out[capo_appflow.types.operator_properties_keys.deserialize_json(key)] = value
    return out
