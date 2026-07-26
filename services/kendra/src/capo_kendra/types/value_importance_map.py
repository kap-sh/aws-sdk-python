"""Generated from Smithy shape ``com.amazonaws.kendra#ValueImportanceMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.importance
    import capo_kendra.types.value_importance_map_key

ValueImportanceMap: TypeAlias = dict[
    "capo_kendra.types.value_importance_map_key.ValueImportanceMapKey",
    "capo_kendra.types.importance.Importance",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ValueImportanceMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ValueImportanceMap:
    out: ValueImportanceMap = {}
    for key, value in data.items():
        out[key] = value
    return out
