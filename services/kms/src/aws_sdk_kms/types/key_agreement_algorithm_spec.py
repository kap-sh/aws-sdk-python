"""Generated from Smithy shape ``com.amazonaws.kms#KeyAgreementAlgorithmSpec``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_kms.errors import DeserializationError

KeyAgreementAlgorithmSpec: TypeAlias = Literal["ECDH",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ECDH",))


def serialize_aws_json_1_1(value: KeyAgreementAlgorithmSpec) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyAgreementAlgorithmSpec:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KeyAgreementAlgorithmSpec value: {data!r}")
    return cast(KeyAgreementAlgorithmSpec, data)
