"""Generated from Smithy shape ``com.amazonaws.macie2#RevealRequestStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The status of a request to retrieve occurrences of sensitive data reported by a finding. Possible values are:</p>"""
RevealRequestStatus: TypeAlias = Literal[
    "SUCCESS",
    "PROCESSING",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESS",
        "PROCESSING",
        "ERROR",
    )
)


def serialize_json(value: RevealRequestStatus) -> str:
    return value


def deserialize_json(data: str) -> RevealRequestStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RevealRequestStatus value: {data!r}")
    return cast(RevealRequestStatus, data)
