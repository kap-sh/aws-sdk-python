"""Generated from Smithy shape ``com.amazonaws.servicequotas#OptInStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_quotas.errors import DeserializationError

OptInStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: OptInStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OptInStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OptInStatus value: {data!r}")
    return cast(OptInStatus, data)
