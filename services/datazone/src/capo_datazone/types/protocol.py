"""Generated from Smithy shape ``com.amazonaws.datazone#Protocol``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: Protocol) -> str:
    return value


def deserialize_json(data: str) -> Protocol:
    return cast(Protocol, data)
