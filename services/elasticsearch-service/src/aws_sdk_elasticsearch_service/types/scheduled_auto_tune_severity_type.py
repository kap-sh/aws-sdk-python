"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ScheduledAutoTuneSeverityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticsearch_service.errors import DeserializationError

"""<p>Specifies Auto-Tune action severity. Valid values are LOW, MEDIUM and HIGH. </p>"""
ScheduledAutoTuneSeverityType: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOW",
        "MEDIUM",
        "HIGH",
    )
)


def serialize_json(value: ScheduledAutoTuneSeverityType) -> str:
    return value


def deserialize_json(data: str) -> ScheduledAutoTuneSeverityType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ScheduledAutoTuneSeverityType value: {data!r}"
        )
    return cast(ScheduledAutoTuneSeverityType, data)
