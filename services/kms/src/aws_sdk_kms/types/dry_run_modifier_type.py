"""Generated from Smithy shape ``com.amazonaws.kms#DryRunModifierType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_kms.errors import DeserializationError

DryRunModifierType: TypeAlias = Literal["IGNORE_CIPHERTEXT",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("IGNORE_CIPHERTEXT",))


def serialize_aws_json_1_1(value: DryRunModifierType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DryRunModifierType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DryRunModifierType value: {data!r}")
    return cast(DryRunModifierType, data)
