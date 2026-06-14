"""Generated from Smithy shape ``com.amazonaws.datazone#Protocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

Protocol: TypeAlias = Literal[
    "ATHENA",
    "GLUE_INTERACTIVE_SESSION",
    "HTTPS",
    "JDBC",
    "LIVY",
    "ODBC",
    "PRISM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ATHENA",
        "GLUE_INTERACTIVE_SESSION",
        "HTTPS",
        "JDBC",
        "LIVY",
        "ODBC",
        "PRISM",
    )
)


def serialize_json(value: Protocol) -> str:
    return value


def deserialize_json(data: str) -> Protocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Protocol value: {data!r}")
    return cast(Protocol, data)
