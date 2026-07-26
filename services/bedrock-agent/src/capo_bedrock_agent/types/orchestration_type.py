"""Generated from Smithy shape ``com.amazonaws.bedrockagent#OrchestrationType``."""

from typing import Literal, TypeAlias, cast

OrchestrationType: TypeAlias = Literal[
    "DEFAULT",
    "CUSTOM_ORCHESTRATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrchestrationType) -> str:
    return value


def deserialize_json(data: str) -> OrchestrationType:
    return cast(OrchestrationType, data)
