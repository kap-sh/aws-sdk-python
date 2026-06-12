"""Generated from Smithy shape ``com.amazonaws.appstream#RequestLimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appstream.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_appstream.types.error_message


class RequestLimitExceededException_(TypedDict):
    message: NotRequired["aws_sdk_appstream.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RequestLimitExceededException_:
    out: RequestLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class RequestLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appstream#RequestLimitExceededException``."""

    code: str | None = "RequestLimitExceededException"

    def __init__(self, data: RequestLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RequestLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "RequestLimitExceededException":
        return cls(deserialize_aws_json_1_1(data))
