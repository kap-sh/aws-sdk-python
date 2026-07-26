"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserEnterprisePolicyType``."""

from typing import Literal, TypeAlias, cast

BrowserEnterprisePolicyType: TypeAlias = Literal[
    "MANAGED",
    "RECOMMENDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: BrowserEnterprisePolicyType) -> str:
    return value


def deserialize_json(data: str) -> BrowserEnterprisePolicyType:
    return cast(BrowserEnterprisePolicyType, data)
