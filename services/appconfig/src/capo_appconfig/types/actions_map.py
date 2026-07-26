"""Generated from Smithy shape ``com.amazonaws.appconfig#ActionsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appconfig.types.action_list
    import capo_appconfig.types.action_point

ActionsMap: TypeAlias = dict[
    "capo_appconfig.types.action_point.ActionPoint",
    "capo_appconfig.types.action_list.ActionList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ActionsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_appconfig.types.action_list
        import capo_appconfig.types.action_point

        out[capo_appconfig.types.action_point.serialize_json(key)] = (
            capo_appconfig.types.action_list.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> ActionsMap:
    out: ActionsMap = {}
    for key, value in data.items():
        import capo_appconfig.types.action_list
        import capo_appconfig.types.action_point

        out[capo_appconfig.types.action_point.deserialize_json(key)] = (
            capo_appconfig.types.action_list.deserialize_json(value)
        )
    return out
