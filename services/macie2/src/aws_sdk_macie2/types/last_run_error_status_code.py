"""Generated from Smithy shape ``com.amazonaws.macie2#LastRunErrorStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>Specifies whether any account- or bucket-level access errors occurred during the run of a one-time classification job or the most recent run of a recurring classification job. Possible values are:</p>"""
LastRunErrorStatusCode: TypeAlias = Literal[
    "NONE",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "ERROR",
    )
)


def serialize_json(value: LastRunErrorStatusCode) -> str:
    return value


def deserialize_json(data: str) -> LastRunErrorStatusCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LastRunErrorStatusCode value: {data!r}")
    return cast(LastRunErrorStatusCode, data)
