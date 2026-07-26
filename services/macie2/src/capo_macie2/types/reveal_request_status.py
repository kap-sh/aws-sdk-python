"""Generated from Smithy shape ``com.amazonaws.macie2#RevealRequestStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a request to retrieve occurrences of sensitive data reported by a finding. Possible values are:</p>"""
RevealRequestStatus: TypeAlias = Literal[
    "SUCCESS",
    "PROCESSING",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: RevealRequestStatus) -> str:
    return value


def deserialize_json(data: str) -> RevealRequestStatus:
    return cast(RevealRequestStatus, data)
