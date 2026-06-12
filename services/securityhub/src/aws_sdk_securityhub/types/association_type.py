"""Generated from Smithy shape ``com.amazonaws.securityhub#AssociationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

AssociationType: TypeAlias = Literal[
    "INHERITED",
    "APPLIED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INHERITED",
        "APPLIED",
    )
)


def serialize_json(value: AssociationType) -> str:
    return value


def deserialize_json(data: str) -> AssociationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssociationType value: {data!r}")
    return cast(AssociationType, data)
