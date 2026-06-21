"""Generated from Smithy shape ``com.amazonaws.appflow#PrefixFormat``."""

from typing import Literal, TypeAlias, cast

PrefixFormat: TypeAlias = Literal[
    "YEAR",
    "MONTH",
    "DAY",
    "HOUR",
    "MINUTE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PrefixFormat) -> str:
    return value


def deserialize_json(data: str) -> PrefixFormat:
    return cast(PrefixFormat, data)
