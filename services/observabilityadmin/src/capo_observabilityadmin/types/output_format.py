"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#OutputFormat``."""

from typing import Literal, TypeAlias, cast

"""<p> Enumeration of supported output formats for ELB access logs: PLAIN for space-delimited format, JSON for structured JSON format. </p>"""
OutputFormat: TypeAlias = Literal[
    "plain",
    "json",
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputFormat) -> str:
    return value


def deserialize_json(data: str) -> OutputFormat:
    return cast(OutputFormat, data)
