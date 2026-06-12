"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#RandomKeyMaxLength``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography_data.errors import DeserializationError

RandomKeyMaxLength: TypeAlias = Literal[
    "BYTES_8",
    "BYTES_16",
    "BYTES_24",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BYTES_8",
        "BYTES_16",
        "BYTES_24",
    )
)


def serialize_json(value: RandomKeyMaxLength) -> str:
    return value


def deserialize_json(data: str) -> RandomKeyMaxLength:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RandomKeyMaxLength value: {data!r}")
    return cast(RandomKeyMaxLength, data)
