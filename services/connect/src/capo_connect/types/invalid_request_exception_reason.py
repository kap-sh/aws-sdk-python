"""Generated from Smithy shape ``com.amazonaws.connect#InvalidRequestExceptionReason``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connect.types.attached_file_invalid_request_exception_reason


class _InvalidRequestExceptionReason_AttachedFileInvalidRequestExceptionReason(
    TypedDict, closed=True
):
    AttachedFileInvalidRequestExceptionReason: "capo_connect.types.attached_file_invalid_request_exception_reason.AttachedFileInvalidRequestExceptionReason"


InvalidRequestExceptionReason: TypeAlias = (
    _InvalidRequestExceptionReason_AttachedFileInvalidRequestExceptionReason
)


# --- restJson1 ser/de ---
def serialize_json(value: InvalidRequestExceptionReason) -> dict:
    if "AttachedFileInvalidRequestExceptionReason" in value:
        import capo_connect.types.attached_file_invalid_request_exception_reason

        return {
            "AttachedFileInvalidRequestExceptionReason": capo_connect.types.attached_file_invalid_request_exception_reason.serialize_json(
                value["AttachedFileInvalidRequestExceptionReason"]
            )
        }
    else:
        raise SerializationError("InvalidRequestExceptionReason: no variant present")


def deserialize_json(data: dict) -> InvalidRequestExceptionReason:
    if "AttachedFileInvalidRequestExceptionReason" in data:
        import capo_connect.types.attached_file_invalid_request_exception_reason

        return {
            "AttachedFileInvalidRequestExceptionReason": capo_connect.types.attached_file_invalid_request_exception_reason.deserialize_json(
                data["AttachedFileInvalidRequestExceptionReason"]
            )
        }
    else:
        raise DeserializationError(
            "InvalidRequestExceptionReason: no recognized variant key"
        )
