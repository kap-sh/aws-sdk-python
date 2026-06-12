"""Generated from Smithy shape ``com.amazonaws.batch#AssignPublicIp``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

AssignPublicIp: TypeAlias = Literal[
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


def serialize_json(value: AssignPublicIp) -> str:
    return value


def deserialize_json(data: str) -> AssignPublicIp:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssignPublicIp value: {data!r}")
    return cast(AssignPublicIp, data)
