"""Generated from Smithy shape ``com.amazonaws.servicequotas#OptInType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_quotas.errors import DeserializationError

OptInType: TypeAlias = Literal[
    "NotifyOnly",
    "NotifyAndAdjust",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NotifyOnly",
        "NotifyAndAdjust",
    )
)


def serialize_aws_json_1_1(value: OptInType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OptInType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OptInType value: {data!r}")
    return cast(OptInType, data)
