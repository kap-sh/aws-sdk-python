"""Generated from Smithy shape ``com.amazonaws.connect#ServiceQuotaExceededExceptionReason``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connect.types.attached_file_service_quota_exceeded_exception_reason


class _ServiceQuotaExceededExceptionReason_AttachedFileServiceQuotaExceededExceptionReason(
    TypedDict, closed=True
):
    AttachedFileServiceQuotaExceededExceptionReason: "capo_connect.types.attached_file_service_quota_exceeded_exception_reason.AttachedFileServiceQuotaExceededExceptionReason"


ServiceQuotaExceededExceptionReason: TypeAlias = (
    _ServiceQuotaExceededExceptionReason_AttachedFileServiceQuotaExceededExceptionReason
)


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededExceptionReason) -> dict:
    if "AttachedFileServiceQuotaExceededExceptionReason" in value:
        import capo_connect.types.attached_file_service_quota_exceeded_exception_reason

        return {
            "AttachedFileServiceQuotaExceededExceptionReason": capo_connect.types.attached_file_service_quota_exceeded_exception_reason.serialize_json(
                value["AttachedFileServiceQuotaExceededExceptionReason"]
            )
        }
    else:
        raise SerializationError(
            "ServiceQuotaExceededExceptionReason: no variant present"
        )


def deserialize_json(data: dict) -> ServiceQuotaExceededExceptionReason:
    if "AttachedFileServiceQuotaExceededExceptionReason" in data:
        import capo_connect.types.attached_file_service_quota_exceeded_exception_reason

        return {
            "AttachedFileServiceQuotaExceededExceptionReason": capo_connect.types.attached_file_service_quota_exceeded_exception_reason.deserialize_json(
                data["AttachedFileServiceQuotaExceededExceptionReason"]
            )
        }
    else:
        raise DeserializationError(
            "ServiceQuotaExceededExceptionReason: no recognized variant key"
        )
