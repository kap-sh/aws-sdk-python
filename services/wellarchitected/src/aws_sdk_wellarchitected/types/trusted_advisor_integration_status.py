"""Generated from Smithy shape ``com.amazonaws.wellarchitected#TrustedAdvisorIntegrationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

TrustedAdvisorIntegrationStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: TrustedAdvisorIntegrationStatus) -> str:
    return value


def deserialize_json(data: str) -> TrustedAdvisorIntegrationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TrustedAdvisorIntegrationStatus value: {data!r}"
        )
    return cast(TrustedAdvisorIntegrationStatus, data)
