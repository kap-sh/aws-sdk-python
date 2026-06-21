"""Generated from Smithy shape ``com.amazonaws.inspector2#IntegrationType``."""

from typing import Literal, TypeAlias, cast

IntegrationType: TypeAlias = Literal[
    "GITLAB_SELF_MANAGED",
    "GITHUB",
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationType) -> str:
    return value


def deserialize_json(data: str) -> IntegrationType:
    return cast(IntegrationType, data)
