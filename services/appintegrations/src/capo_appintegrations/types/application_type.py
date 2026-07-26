"""Generated from Smithy shape ``com.amazonaws.appintegrations#ApplicationType``."""

from typing import Literal, TypeAlias, cast

"""<value>The type of application</value>"""
ApplicationType: TypeAlias = Literal[
    "STANDARD",
    "SERVICE",
    "MCP_SERVER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationType) -> str:
    return value


def deserialize_json(data: str) -> ApplicationType:
    return cast(ApplicationType, data)
