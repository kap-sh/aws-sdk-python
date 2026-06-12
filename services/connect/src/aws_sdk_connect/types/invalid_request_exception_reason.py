"""Generated from Smithy shape ``com.amazonaws.connect#InvalidRequestExceptionReason``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.attached_file_invalid_request_exception_reason


class _InvalidRequestExceptionReason_AttachedFileInvalidRequestExceptionReason(
    TypedDict
):
    AttachedFileInvalidRequestExceptionReason: "aws_sdk_connect.types.attached_file_invalid_request_exception_reason.AttachedFileInvalidRequestExceptionReason"


InvalidRequestExceptionReason: TypeAlias = (
    _InvalidRequestExceptionReason_AttachedFileInvalidRequestExceptionReason
)


# --- restJson1 ser/de ---
def serialize_json(value: InvalidRequestExceptionReason) -> dict:
    if "AttachedFileInvalidRequestExceptionReason" in value:
        import aws_sdk_connect.types.attached_file_invalid_request_exception_reason

        return {
            "AttachedFileInvalidRequestExceptionReason": aws_sdk_connect.types.attached_file_invalid_request_exception_reason.serialize_json(
                value["AttachedFileInvalidRequestExceptionReason"]
            )
        }
    else:
        raise SerializationError("InvalidRequestExceptionReason: no variant present")


def deserialize_json(data: dict) -> InvalidRequestExceptionReason:
    if "AttachedFileInvalidRequestExceptionReason" in data:
        import aws_sdk_connect.types.attached_file_invalid_request_exception_reason

        return {
            "AttachedFileInvalidRequestExceptionReason": aws_sdk_connect.types.attached_file_invalid_request_exception_reason.deserialize_json(
                data["AttachedFileInvalidRequestExceptionReason"]
            )
        }
    else:
        raise DeserializationError(
            "InvalidRequestExceptionReason: no recognized variant key"
        )
