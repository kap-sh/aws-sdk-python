"""Generated from Smithy shape ``com.amazonaws.ebs#ServiceQuotaExceededExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ebs.errors import DeserializationError

ServiceQuotaExceededExceptionReason: TypeAlias = Literal[
    "DEPENDENCY_SERVICE_QUOTA_EXCEEDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DEPENDENCY_SERVICE_QUOTA_EXCEEDED",))


def serialize_json(value: ServiceQuotaExceededExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ServiceQuotaExceededExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ServiceQuotaExceededExceptionReason value: {data!r}"
        )
    return cast(ServiceQuotaExceededExceptionReason, data)
