"""Generated from Smithy shape ``com.amazonaws.batch#OrchestrationType``."""

from typing import Literal, TypeAlias, cast

OrchestrationType: TypeAlias = Literal[
    "ECS",
    "EKS",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrchestrationType) -> str:
    return value


def deserialize_json(data: str) -> OrchestrationType:
    return cast(OrchestrationType, data)
