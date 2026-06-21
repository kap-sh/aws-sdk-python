"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ScheduledAutoTuneSeverityType``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies Auto-Tune action severity. Valid values are LOW, MEDIUM and HIGH. </p>"""
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
