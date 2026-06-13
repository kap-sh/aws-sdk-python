"""Generated from Smithy shape ``com.amazonaws.inspector2#CisRuleDetails``."""

import base64
from typing import TypeAlias

CisRuleDetails: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: CisRuleDetails) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> CisRuleDetails:
    return base64.b64decode(data)
