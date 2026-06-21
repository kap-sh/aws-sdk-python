"""Generated from Smithy shape ``com.amazonaws.opensearch#TimeUnit``."""

from typing import Literal, TypeAlias, cast

"""<p>The unit of a maintenance schedule duration. Valid value is <code>HOUR</code>.</p>"""
TimeUnit: TypeAlias = Literal["HOURS",]


# --- restJson1 ser/de ---
def serialize_json(value: TimeUnit) -> str:
    return value


def deserialize_json(data: str) -> TimeUnit:
    return cast(TimeUnit, data)
