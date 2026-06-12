"""Generated from Smithy shape ``com.amazonaws.opensearch#CapabilityFailureReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

CapabilityFailureReason: TypeAlias = Literal["KMS_KEY_INSUFFICIENT_PERMISSION",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("KMS_KEY_INSUFFICIENT_PERMISSION",))


def serialize_json(value: CapabilityFailureReason) -> str:
    return value


def deserialize_json(data: str) -> CapabilityFailureReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapabilityFailureReason value: {data!r}")
    return cast(CapabilityFailureReason, data)
