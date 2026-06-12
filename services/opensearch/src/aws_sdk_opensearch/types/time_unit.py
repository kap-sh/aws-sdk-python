"""Generated from Smithy shape ``com.amazonaws.opensearch#TimeUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

"""<p>The unit of a maintenance schedule duration. Valid value is <code>HOUR</code>.</p>"""
TimeUnit: TypeAlias = Literal["HOURS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("HOURS",))


def serialize_json(value: TimeUnit) -> str:
    return value


def deserialize_json(data: str) -> TimeUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TimeUnit value: {data!r}")
    return cast(TimeUnit, data)
