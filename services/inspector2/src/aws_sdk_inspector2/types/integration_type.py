"""Generated from Smithy shape ``com.amazonaws.inspector2#IntegrationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

IntegrationType: TypeAlias = Literal[
    "GITLAB_SELF_MANAGED",
    "GITHUB",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GITLAB_SELF_MANAGED",
        "GITHUB",
    )
)


def serialize_json(value: IntegrationType) -> str:
    return value


def deserialize_json(data: str) -> IntegrationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IntegrationType value: {data!r}")
    return cast(IntegrationType, data)
