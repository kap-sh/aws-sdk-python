"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ParentBotNetworks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.parent_bot_network

ParentBotNetworks: TypeAlias = list[
    "capo_lex_models_v2.types.parent_bot_network.ParentBotNetwork"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParentBotNetworks) -> list:
    import capo_lex_models_v2.types.parent_bot_network

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.parent_bot_network.serialize_json(item))
    return out


def deserialize_json(data: list) -> ParentBotNetworks:
    import capo_lex_models_v2.types.parent_bot_network

    out: ParentBotNetworks = []
    for item in data:
        out.append(capo_lex_models_v2.types.parent_bot_network.deserialize_json(item))
    return out
