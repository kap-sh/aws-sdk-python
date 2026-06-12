"""Generated from Smithy shape ``com.amazonaws.macie2#OriginType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>Specifies how Amazon Macie found the sensitive data that produced a finding. Possible values are:</p>"""
OriginType: TypeAlias = Literal[
    "SENSITIVE_DATA_DISCOVERY_JOB",
    "AUTOMATED_SENSITIVE_DATA_DISCOVERY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SENSITIVE_DATA_DISCOVERY_JOB",
        "AUTOMATED_SENSITIVE_DATA_DISCOVERY",
    )
)


def serialize_json(value: OriginType) -> str:
    return value


def deserialize_json(data: str) -> OriginType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OriginType value: {data!r}")
    return cast(OriginType, data)
