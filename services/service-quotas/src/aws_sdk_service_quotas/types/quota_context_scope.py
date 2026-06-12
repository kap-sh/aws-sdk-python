"""Generated from Smithy shape ``com.amazonaws.servicequotas#QuotaContextScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_quotas.errors import DeserializationError

QuotaContextScope: TypeAlias = Literal[
    "RESOURCE",
    "ACCOUNT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESOURCE",
        "ACCOUNT",
    )
)


def serialize_aws_json_1_1(value: QuotaContextScope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QuotaContextScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QuotaContextScope value: {data!r}")
    return cast(QuotaContextScope, data)
