"""Generated from Smithy shape ``com.amazonaws.macie2#RevealStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of the configuration for retrieving occurrences of sensitive data reported by findings. Valid values are:</p>"""
RevealStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RevealStatus) -> str:
    return value


def deserialize_json(data: str) -> RevealStatus:
    return cast(RevealStatus, data)
