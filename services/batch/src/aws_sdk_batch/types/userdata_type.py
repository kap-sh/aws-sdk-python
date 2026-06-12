"""Generated from Smithy shape ``com.amazonaws.batch#UserdataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

UserdataType: TypeAlias = Literal[
    "EKS_BOOTSTRAP_SH",
    "EKS_NODEADM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EKS_BOOTSTRAP_SH",
        "EKS_NODEADM",
    )
)


def serialize_json(value: UserdataType) -> str:
    return value


def deserialize_json(data: str) -> UserdataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserdataType value: {data!r}")
    return cast(UserdataType, data)
