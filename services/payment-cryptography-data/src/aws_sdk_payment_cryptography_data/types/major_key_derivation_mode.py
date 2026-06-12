"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#MajorKeyDerivationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography_data.errors import DeserializationError

MajorKeyDerivationMode: TypeAlias = Literal[
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


def serialize_json(value: MajorKeyDerivationMode) -> str:
    return value


def deserialize_json(data: str) -> MajorKeyDerivationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MajorKeyDerivationMode value: {data!r}")
    return cast(MajorKeyDerivationMode, data)
