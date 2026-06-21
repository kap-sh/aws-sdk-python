"""Generated from Smithy shape ``com.amazonaws.elementalinference#OutputStatus``."""

from typing import Literal, TypeAlias, cast

OutputStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputStatus) -> str:
    return value


def deserialize_json(data: str) -> OutputStatus:
    return cast(OutputStatus, data)
