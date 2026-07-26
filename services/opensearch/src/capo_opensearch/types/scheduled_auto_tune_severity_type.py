"""Generated from Smithy shape ``com.amazonaws.opensearch#ScheduledAutoTuneSeverityType``."""

from typing import Literal, TypeAlias, cast

"""<p>The Auto-Tune action severity.</p>"""
ScheduledAutoTuneSeverityType: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduledAutoTuneSeverityType) -> str:
    return value


def deserialize_json(data: str) -> ScheduledAutoTuneSeverityType:
    return cast(ScheduledAutoTuneSeverityType, data)
