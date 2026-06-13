"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AutoApprovedChangeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

AutoApprovedChangeType: TypeAlias = Literal[
    "ADD_MEMBER",
    "GRANT_RECEIVE_RESULTS_ABILITY",
    "REVOKE_RECEIVE_RESULTS_ABILITY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ADD_MEMBER",
        "GRANT_RECEIVE_RESULTS_ABILITY",
        "REVOKE_RECEIVE_RESULTS_ABILITY",
    )
)


def serialize_json(value: AutoApprovedChangeType) -> str:
    return value


def deserialize_json(data: str) -> AutoApprovedChangeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoApprovedChangeType value: {data!r}")
    return cast(AutoApprovedChangeType, data)
