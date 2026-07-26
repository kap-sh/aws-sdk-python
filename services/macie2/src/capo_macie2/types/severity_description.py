"""Generated from Smithy shape ``com.amazonaws.macie2#SeverityDescription``."""

from typing import Literal, TypeAlias, cast

"""<p>The qualitative representation of the finding's severity. Possible values are:</p>"""
SeverityDescription: TypeAlias = Literal[
    "Low",
    "Medium",
    "High",
]


# --- restJson1 ser/de ---
def serialize_json(value: SeverityDescription) -> str:
    return value


def deserialize_json(data: str) -> SeverityDescription:
    return cast(SeverityDescription, data)
