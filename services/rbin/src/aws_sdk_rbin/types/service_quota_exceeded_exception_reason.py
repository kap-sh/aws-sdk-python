"""Generated from Smithy shape ``com.amazonaws.rbin#ServiceQuotaExceededExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rbin.errors import DeserializationError

ServiceQuotaExceededExceptionReason: TypeAlias = Literal["SERVICE_QUOTA_EXCEEDED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SERVICE_QUOTA_EXCEEDED",))


def serialize_json(value: ServiceQuotaExceededExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ServiceQuotaExceededExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ServiceQuotaExceededExceptionReason value: {data!r}"
        )
    return cast(ServiceQuotaExceededExceptionReason, data)
