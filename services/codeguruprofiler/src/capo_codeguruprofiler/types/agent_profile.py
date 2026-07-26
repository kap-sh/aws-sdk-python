"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#AgentProfile``."""

import base64
from typing import TypeAlias

AgentProfile: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: AgentProfile) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> AgentProfile:
    return base64.b64decode(data)
