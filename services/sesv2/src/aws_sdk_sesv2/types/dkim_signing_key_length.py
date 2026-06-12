"""Generated from Smithy shape ``com.amazonaws.sesv2#DkimSigningKeyLength``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

DkimSigningKeyLength: TypeAlias = Literal[
    "RSA_1024_BIT",
    "RSA_2048_BIT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RSA_1024_BIT",
        "RSA_2048_BIT",
    )
)


def serialize_json(value: DkimSigningKeyLength) -> str:
    return value


def deserialize_json(data: str) -> DkimSigningKeyLength:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DkimSigningKeyLength value: {data!r}")
    return cast(DkimSigningKeyLength, data)
