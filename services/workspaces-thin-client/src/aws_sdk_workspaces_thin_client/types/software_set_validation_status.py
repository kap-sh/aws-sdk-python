"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#SoftwareSetValidationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_thin_client.errors import DeserializationError

SoftwareSetValidationStatus: TypeAlias = Literal[
    "VALIDATED",
    "NOT_VALIDATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VALIDATED",
        "NOT_VALIDATED",
    )
)


def serialize_json(value: SoftwareSetValidationStatus) -> str:
    return value


def deserialize_json(data: str) -> SoftwareSetValidationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SoftwareSetValidationStatus value: {data!r}"
        )
    return cast(SoftwareSetValidationStatus, data)
