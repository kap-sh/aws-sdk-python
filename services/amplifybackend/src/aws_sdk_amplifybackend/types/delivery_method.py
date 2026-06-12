"""Generated from Smithy shape ``com.amazonaws.amplifybackend#DeliveryMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifybackend.errors import DeserializationError

"""<p>The type of verification message to send.</p>"""
DeliveryMethod: TypeAlias = Literal[
    "EMAIL",
    "SMS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EMAIL",
        "SMS",
    )
)


def serialize_json(value: DeliveryMethod) -> str:
    return value


def deserialize_json(data: str) -> DeliveryMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeliveryMethod value: {data!r}")
    return cast(DeliveryMethod, data)
