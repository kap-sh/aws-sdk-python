"""Generated from Smithy shape ``com.amazonaws.devopsagent#NewRelicRegion``."""

from typing import Literal, TypeAlias, cast

"""<p>The NewRelic region (determines API endpoint).</p>"""
NewRelicRegion: TypeAlias = Literal[
    "US",
    "EU",
]


# --- restJson1 ser/de ---
def serialize_json(value: NewRelicRegion) -> str:
    return value


def deserialize_json(data: str) -> NewRelicRegion:
    return cast(NewRelicRegion, data)
