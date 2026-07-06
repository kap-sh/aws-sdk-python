"""Generated from Smithy shape ``com.amazonaws.appstream#IncompatibleImageException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appstream.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_appstream.types.error_message


class IncompatibleImageException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_appstream.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IncompatibleImageException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IncompatibleImageException_:
    out: IncompatibleImageException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class IncompatibleImageException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appstream#IncompatibleImageException``."""

    code: str | None = "IncompatibleImageException"

    def __init__(self, data: IncompatibleImageException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IncompatibleImageException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "IncompatibleImageException":
        return cls(deserialize_aws_json_1_1(data))
