"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SynchronizationType``."""

from typing import Literal, TypeAlias, cast

SynchronizationType: TypeAlias = Literal["URL",]


# --- restJson1 ser/de ---
def serialize_json(value: SynchronizationType) -> str:
    return value


def deserialize_json(data: str) -> SynchronizationType:
    return cast(SynchronizationType, data)
