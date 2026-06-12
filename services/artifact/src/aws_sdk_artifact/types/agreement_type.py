"""Generated from Smithy shape ``com.amazonaws.artifact#AgreementType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_artifact.errors import DeserializationError

AgreementType: TypeAlias = Literal[
    "CUSTOM",
    "DEFAULT",
    "MODIFIED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOM",
        "DEFAULT",
        "MODIFIED",
    )
)


def serialize_json(value: AgreementType) -> str:
    return value


def deserialize_json(data: str) -> AgreementType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgreementType value: {data!r}")
    return cast(AgreementType, data)
