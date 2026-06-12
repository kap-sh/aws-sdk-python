"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#AssociationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

AssociationState: TypeAlias = Literal[
    "ASSOCIATION_IN_PROGRESS",
    "ASSOCIATION_FAILED",
    "ASSOCIATION_SUCCEEDED",
    "ASSOCIATION_DELETING",
    "REFRESH_TOKEN_EXPIRED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSOCIATION_IN_PROGRESS",
        "ASSOCIATION_FAILED",
        "ASSOCIATION_SUCCEEDED",
        "ASSOCIATION_DELETING",
        "REFRESH_TOKEN_EXPIRED",
    )
)


def serialize_json(value: AssociationState) -> str:
    return value


def deserialize_json(data: str) -> AssociationState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssociationState value: {data!r}")
    return cast(AssociationState, data)
