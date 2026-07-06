"""Generated from Smithy shape ``com.amazonaws.pi#NotAuthorizedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pi.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_pi.types.error_string


class NotAuthorizedException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_pi.types.error_string.ErrorString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotAuthorizedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NotAuthorizedException_:
    out: NotAuthorizedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class NotAuthorizedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pi#NotAuthorizedException``."""

    code: str | None = "NotAuthorizedException"

    def __init__(self, data: NotAuthorizedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotAuthorizedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "NotAuthorizedException":
        return cls(deserialize_aws_json_1_1(data))
