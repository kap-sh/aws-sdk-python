"""Generated from Smithy shape ``com.amazonaws.lightsail#BPAStatusMessage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

BPAStatusMessage: TypeAlias = Literal[
    "DEFAULTED_FOR_SLR_MISSING",
    "SYNC_ON_HOLD",
    "DEFAULTED_FOR_SLR_MISSING_ON_HOLD",
    "Unknown",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULTED_FOR_SLR_MISSING",
        "SYNC_ON_HOLD",
        "DEFAULTED_FOR_SLR_MISSING_ON_HOLD",
        "Unknown",
    )
)


def serialize_aws_json_1_1(value: BPAStatusMessage) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BPAStatusMessage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BPAStatusMessage value: {data!r}")
    return cast(BPAStatusMessage, data)
