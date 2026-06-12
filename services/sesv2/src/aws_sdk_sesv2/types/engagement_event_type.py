"""Generated from Smithy shape ``com.amazonaws.sesv2#EngagementEventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

"""<p>The type of delivery events:</p> <ul> <li> <p> <code>OPEN</code> - Open event for emails including open trackers. Excludes opens for emails addressed to more than one recipient.</p> </li> <li> <p> <code>CLICK</code> - Click event for emails including wrapped links. Excludes clicks for emails addressed to more than one recipient.</p> </li> </ul>"""
EngagementEventType: TypeAlias = Literal[
    "OPEN",
    "CLICK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OPEN",
        "CLICK",
    )
)


def serialize_json(value: EngagementEventType) -> str:
    return value


def deserialize_json(data: str) -> EngagementEventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EngagementEventType value: {data!r}")
    return cast(EngagementEventType, data)
