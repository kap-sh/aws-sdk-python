"""Generated from Smithy shape ``com.amazonaws.novaact#ModelAliases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.model_alias

ModelAliases: TypeAlias = list["aws_sdk_nova_act.types.model_alias.ModelAlias"]


# --- restJson1 ser/de ---
def serialize_json(value: ModelAliases) -> list:
    import aws_sdk_nova_act.types.model_alias

    out: list = []
    for item in value:
        out.append(aws_sdk_nova_act.types.model_alias.serialize_json(item))
    return out


def deserialize_json(data: list) -> ModelAliases:
    import aws_sdk_nova_act.types.model_alias

    out: ModelAliases = []
    for item in data:
        out.append(aws_sdk_nova_act.types.model_alias.deserialize_json(item))
    return out
