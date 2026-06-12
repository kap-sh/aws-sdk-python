"""Generated from Smithy shape ``com.amazonaws.iotwireless#SigningAlg``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

"""<p>The certificate chain algorithm provided by sidewalk.</p>"""
SigningAlg: TypeAlias = Literal[
    "Ed25519",
    "P256r1",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Ed25519",
        "P256r1",
    )
)


def serialize_json(value: SigningAlg) -> str:
    return value


def deserialize_json(data: str) -> SigningAlg:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SigningAlg value: {data!r}")
    return cast(SigningAlg, data)
