"""Generated from Smithy shape ``com.amazonaws.batch#ServiceJobRetryAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

ServiceJobRetryAction: TypeAlias = Literal[
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


def serialize_json(value: ServiceJobRetryAction) -> str:
    return value


def deserialize_json(data: str) -> ServiceJobRetryAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceJobRetryAction value: {data!r}")
    return cast(ServiceJobRetryAction, data)
