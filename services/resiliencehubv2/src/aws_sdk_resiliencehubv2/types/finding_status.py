"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#FindingStatus``."""

from typing import Literal, TypeAlias, cast

FindingStatus: TypeAlias = Literal[
    "OPEN",
    "RESOLVED",
    "IRRELEVANT",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingStatus) -> str:
    return value


def deserialize_json(data: str) -> FindingStatus:
    return cast(FindingStatus, data)
