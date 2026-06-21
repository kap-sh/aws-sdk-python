"""Generated from Smithy shape ``com.amazonaws.macie2#AvailabilityCode``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies whether occurrences of sensitive data can be retrieved for a finding. Possible values are:</p>"""
AvailabilityCode: TypeAlias = Literal[
    "AVAILABLE",
    "UNAVAILABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AvailabilityCode) -> str:
    return value


def deserialize_json(data: str) -> AvailabilityCode:
    return cast(AvailabilityCode, data)
