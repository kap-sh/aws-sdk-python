"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyValidationMode``."""

from typing import Literal, TypeAlias, cast

PolicyValidationMode: TypeAlias = Literal[
    "FAIL_ON_ANY_FINDINGS",
    "IGNORE_ALL_FINDINGS",
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyValidationMode) -> str:
    return value


def deserialize_json(data: str) -> PolicyValidationMode:
    return cast(PolicyValidationMode, data)
