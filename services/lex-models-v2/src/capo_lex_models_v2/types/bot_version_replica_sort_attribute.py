"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotVersionReplicaSortAttribute``."""

from typing import Literal, TypeAlias, cast

BotVersionReplicaSortAttribute: TypeAlias = Literal["BotVersion",]


# --- restJson1 ser/de ---
def serialize_json(value: BotVersionReplicaSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> BotVersionReplicaSortAttribute:
    return cast(BotVersionReplicaSortAttribute, data)
