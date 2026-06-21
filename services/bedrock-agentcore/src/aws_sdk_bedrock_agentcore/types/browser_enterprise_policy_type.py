"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserEnterprisePolicyType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of browser enterprise policy. Available values are <code>MANAGED</code> and <code>RECOMMENDED</code>.</p>"""
BrowserEnterprisePolicyType: TypeAlias = Literal[
    "MANAGED",
    "RECOMMENDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: BrowserEnterprisePolicyType) -> str:
    return value


def deserialize_json(data: str) -> BrowserEnterprisePolicyType:
    return cast(BrowserEnterprisePolicyType, data)
