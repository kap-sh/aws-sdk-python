"""Generated from Smithy shape ``com.amazonaws.bedrock#AgreementStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

AgreementStatus: TypeAlias = Literal[
    "AVAILABLE",
    "PENDING",
    "NOT_AVAILABLE",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "PENDING",
        "NOT_AVAILABLE",
        "ERROR",
    )
)


def serialize_json(value: AgreementStatus) -> str:
    return value


def deserialize_json(data: str) -> AgreementStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgreementStatus value: {data!r}")
    return cast(AgreementStatus, data)
