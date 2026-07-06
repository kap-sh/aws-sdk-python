"""Generated from Smithy shape ``com.amazonaws.athena#SessionAlreadyExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_athena.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_athena.types.error_message


class SessionAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_athena.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionAlreadyExistsException_:
    out: SessionAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class SessionAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.athena#SessionAlreadyExistsException``."""

    code: str | None = "SessionAlreadyExistsException"

    def __init__(self, data: SessionAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SessionAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "SessionAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data))
