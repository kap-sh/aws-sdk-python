"""Generated from Smithy shape ``com.amazonaws.macie2#OriginType``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies how Amazon Macie found the sensitive data that produced a finding. Possible values are:</p>"""
OriginType: TypeAlias = Literal[
    "SENSITIVE_DATA_DISCOVERY_JOB",
    "AUTOMATED_SENSITIVE_DATA_DISCOVERY",
]


# --- restJson1 ser/de ---
def serialize_json(value: OriginType) -> str:
    return value


def deserialize_json(data: str) -> OriginType:
    return cast(OriginType, data)
