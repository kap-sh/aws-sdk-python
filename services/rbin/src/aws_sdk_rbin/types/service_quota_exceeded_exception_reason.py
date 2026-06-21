"""Generated from Smithy shape ``com.amazonaws.rbin#ServiceQuotaExceededExceptionReason``."""

from typing import Literal, TypeAlias, cast

ServiceQuotaExceededExceptionReason: TypeAlias = Literal["SERVICE_QUOTA_EXCEEDED",]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ServiceQuotaExceededExceptionReason:
    return cast(ServiceQuotaExceededExceptionReason, data)
