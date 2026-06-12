"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#OutputFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_observabilityadmin.errors import DeserializationError

"""<p> Enumeration of supported output formats for ELB access logs: PLAIN for space-delimited format, JSON for structured JSON format. </p>"""
OutputFormat: TypeAlias = Literal[
    "plain",
    "json",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "plain",
        "json",
    )
)


def serialize_json(value: OutputFormat) -> str:
    return value


def deserialize_json(data: str) -> OutputFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OutputFormat value: {data!r}")
    return cast(OutputFormat, data)
