"""Generated from Smithy shape ``com.amazonaws.mediastore#InternalServerError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mediastore.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.error_message


class InternalServerError_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_mediastore.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalServerError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalServerError_:
    out: InternalServerError_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InternalServerError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediastore#InternalServerError``."""

    code: str | None = "InternalServerError"

    def __init__(self, data: InternalServerError_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerError",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InternalServerError":
        return cls(deserialize_aws_json_1_1(data))
