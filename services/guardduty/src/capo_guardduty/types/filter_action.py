"""Generated from Smithy shape ``com.amazonaws.guardduty#FilterAction``."""

from typing import Literal, TypeAlias, cast

FilterAction: TypeAlias = Literal[
    "NOOP",
    "ARCHIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterAction) -> str:
    return value


def deserialize_json(data: str) -> FilterAction:
    return cast(FilterAction, data)
