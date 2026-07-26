"""Generated from Smithy shape ``com.amazonaws.fis#ActionTargetMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.action_target
    import capo_fis.types.action_target_name

ActionTargetMap: TypeAlias = dict[
    "capo_fis.types.action_target_name.ActionTargetName",
    "capo_fis.types.action_target.ActionTarget",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ActionTargetMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_fis.types.action_target

        out[key] = capo_fis.types.action_target.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ActionTargetMap:
    out: ActionTargetMap = {}
    for key, value in data.items():
        import capo_fis.types.action_target

        out[key] = capo_fis.types.action_target.deserialize_json(value)
    return out
