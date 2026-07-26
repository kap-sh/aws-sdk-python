"""Generated from Smithy shape ``com.amazonaws.securityagent#FindingStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Finding status.</p>"""
FindingStatus: TypeAlias = Literal[
    "ACTIVE",
    "RESOLVED",
    "ACCEPTED",
    "FALSE_POSITIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingStatus) -> str:
    return value


def deserialize_json(data: str) -> FindingStatus:
    return cast(FindingStatus, data)
