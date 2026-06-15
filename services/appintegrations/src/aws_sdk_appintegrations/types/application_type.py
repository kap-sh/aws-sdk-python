"""Generated from Smithy shape ``com.amazonaws.appintegrations#ApplicationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appintegrations.errors import DeserializationError

"""<value>The type of application</value>"""
ApplicationType: TypeAlias = Literal[
    "STANDARD",
    "SERVICE",
    "MCP_SERVER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "SERVICE",
        "MCP_SERVER",
    )
)


def serialize_json(value: ApplicationType) -> str:
    return value


def deserialize_json(data: str) -> ApplicationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationType value: {data!r}")
    return cast(ApplicationType, data)
