"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#AggregatedProfile``."""

import base64
from typing import TypeAlias

AggregatedProfile: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: AggregatedProfile) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> AggregatedProfile:
    return base64.b64decode(data)
