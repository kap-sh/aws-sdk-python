"""Generated from Smithy shape ``com.amazonaws.opensearch#CapabilityFailureReason``."""

from typing import Literal, TypeAlias, cast

CapabilityFailureReason: TypeAlias = Literal["KMS_KEY_INSUFFICIENT_PERMISSION",]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityFailureReason) -> str:
    return value


def deserialize_json(data: str) -> CapabilityFailureReason:
    return cast(CapabilityFailureReason, data)
