"""Generated from Smithy shape ``com.amazonaws.batch#RetryAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

RetryAction: TypeAlias = Literal[
    "RETRY",
    "EXIT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RETRY",
        "EXIT",
    )
)


def serialize_json(value: RetryAction) -> str:
    return value


def deserialize_json(data: str) -> RetryAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RetryAction value: {data!r}")
    return cast(RetryAction, data)
