"""Generated from Smithy shape ``com.amazonaws.appconfig#ActionsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.action_list
    import aws_sdk_appconfig.types.action_point

ActionsMap: TypeAlias = dict[
    "aws_sdk_appconfig.types.action_point.ActionPoint",
    "aws_sdk_appconfig.types.action_list.ActionList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ActionsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_appconfig.types.action_list
        import aws_sdk_appconfig.types.action_point

        out[aws_sdk_appconfig.types.action_point.serialize_json(key)] = (
            aws_sdk_appconfig.types.action_list.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> ActionsMap:
    out: ActionsMap = {}
    for key, value in data.items():
        import aws_sdk_appconfig.types.action_list
        import aws_sdk_appconfig.types.action_point

        out[aws_sdk_appconfig.types.action_point.deserialize_json(key)] = (
            aws_sdk_appconfig.types.action_list.deserialize_json(value)
        )
    return out
