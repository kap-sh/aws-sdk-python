"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#EmvMajorKeyDerivationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography_data.errors import DeserializationError

EmvMajorKeyDerivationMode: TypeAlias = Literal[
    "EMV_OPTION_A",
    "EMV_OPTION_B",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EMV_OPTION_A",
        "EMV_OPTION_B",
    )
)


def serialize_json(value: EmvMajorKeyDerivationMode) -> str:
    return value


def deserialize_json(data: str) -> EmvMajorKeyDerivationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EmvMajorKeyDerivationMode value: {data!r}")
    return cast(EmvMajorKeyDerivationMode, data)
