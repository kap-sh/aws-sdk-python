"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#SoftwareSetUpdateMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_thin_client.errors import DeserializationError

SoftwareSetUpdateMode: TypeAlias = Literal[
    "USE_LATEST",
    "USE_DESIRED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USE_LATEST",
        "USE_DESIRED",
    )
)


def serialize_json(value: SoftwareSetUpdateMode) -> str:
    return value


def deserialize_json(data: str) -> SoftwareSetUpdateMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SoftwareSetUpdateMode value: {data!r}")
    return cast(SoftwareSetUpdateMode, data)
