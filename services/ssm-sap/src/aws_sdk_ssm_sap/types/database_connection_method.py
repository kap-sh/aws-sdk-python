"""Generated from Smithy shape ``com.amazonaws.ssmsap#DatabaseConnectionMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

DatabaseConnectionMethod: TypeAlias = Literal[
    "DIRECT",
    "OVERLAY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DIRECT",
        "OVERLAY",
    )
)


def serialize_json(value: DatabaseConnectionMethod) -> str:
    return value


def deserialize_json(data: str) -> DatabaseConnectionMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatabaseConnectionMethod value: {data!r}")
    return cast(DatabaseConnectionMethod, data)
