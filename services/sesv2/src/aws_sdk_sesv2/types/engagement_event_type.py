"""Generated from Smithy shape ``com.amazonaws.sesv2#EngagementEventType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of delivery events:</p> <ul> <li> <p> <code>OPEN</code> - Open event for emails including open trackers. Excludes opens for emails addressed to more than one recipient.</p> </li> <li> <p> <code>CLICK</code> - Click event for emails including wrapped links. Excludes clicks for emails addressed to more than one recipient.</p> </li> </ul>"""
EngagementEventType: TypeAlias = Literal[
    "OPEN",
    "CLICK",
]


# --- restJson1 ser/de ---
def serialize_json(value: EngagementEventType) -> str:
    return value


def deserialize_json(data: str) -> EngagementEventType:
    return cast(EngagementEventType, data)
