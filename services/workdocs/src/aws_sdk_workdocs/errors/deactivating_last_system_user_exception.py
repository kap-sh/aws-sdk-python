"""Generated from Smithy shape ``com.amazonaws.workdocs#DeactivatingLastSystemUserException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workdocs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.error_message_type
    import aws_sdk_workdocs.types.exception_code_type


class DeactivatingLastSystemUserException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_workdocs.types.error_message_type.ErrorMessageType"]
    code: NotRequired["aws_sdk_workdocs.types.exception_code_type.ExceptionCodeType"]


# --- restJson1 ser/de ---
def serialize_json(value: DeactivatingLastSystemUserException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    return out


def deserialize_json(data: dict) -> DeactivatingLastSystemUserException_:
    out: DeactivatingLastSystemUserException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Code" in data:
        out["code"] = data["Code"]
    return out


class DeactivatingLastSystemUserException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workdocs#DeactivatingLastSystemUserException``."""

    code: str | None = "DeactivatingLastSystemUserException"

    def __init__(self, data: DeactivatingLastSystemUserException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DeactivatingLastSystemUserException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DeactivatingLastSystemUserException":
        return cls(deserialize_json(data))
