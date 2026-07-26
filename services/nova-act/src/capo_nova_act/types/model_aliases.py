"""Generated from Smithy shape ``com.amazonaws.novaact#ModelAliases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_nova_act.types.model_alias

ModelAliases: TypeAlias = list["capo_nova_act.types.model_alias.ModelAlias"]


# --- restJson1 ser/de ---
def serialize_json(value: ModelAliases) -> list:
    import capo_nova_act.types.model_alias

    out: list = []
    for item in value:
        out.append(capo_nova_act.types.model_alias.serialize_json(item))
    return out


def deserialize_json(data: list) -> ModelAliases:
    import capo_nova_act.types.model_alias

    out: ModelAliases = []
    for item in data:
        out.append(capo_nova_act.types.model_alias.deserialize_json(item))
    return out
