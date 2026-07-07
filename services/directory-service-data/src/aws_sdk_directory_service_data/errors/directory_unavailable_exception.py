"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#DirectoryUnavailableException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_directory_service_data.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_directory_service_data.types.directory_unavailable_reason
    import aws_sdk_directory_service_data.types.exception_message


class DirectoryUnavailableException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_directory_service_data.types.exception_message.ExceptionMessage"
    ]
    reason: NotRequired[
        "aws_sdk_directory_service_data.types.directory_unavailable_reason.DirectoryUnavailableReason"
    ]
    """<p> Reason the request failed for the specified directory. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DirectoryUnavailableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import aws_sdk_directory_service_data.types.directory_unavailable_reason

        out["Reason"] = (
            aws_sdk_directory_service_data.types.directory_unavailable_reason.serialize_json(
                value["reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> DirectoryUnavailableException_:
    out: DirectoryUnavailableException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        import aws_sdk_directory_service_data.types.directory_unavailable_reason

        out["reason"] = (
            aws_sdk_directory_service_data.types.directory_unavailable_reason.deserialize_json(
                data["Reason"]
            )
        )
    return out


class DirectoryUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.directoryservicedata#DirectoryUnavailableException``."""

    code: str | None = "DirectoryUnavailableException"

    def __init__(self, data: DirectoryUnavailableException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="DirectoryUnavailableException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DirectoryUnavailableException":
        return cls(deserialize_json(data))
