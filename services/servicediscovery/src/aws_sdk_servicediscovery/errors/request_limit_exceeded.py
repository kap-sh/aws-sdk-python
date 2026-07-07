"""Generated from Smithy shape ``com.amazonaws.servicediscovery#RequestLimitExceeded``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_servicediscovery.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.error_message


class RequestLimitExceeded_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_servicediscovery.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestLimitExceeded_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RequestLimitExceeded_:
    out: RequestLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class RequestLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicediscovery#RequestLimitExceeded``."""

    code: str | None = "RequestLimitExceeded"

    def __init__(self, data: RequestLimitExceeded_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RequestLimitExceeded",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "RequestLimitExceeded":
        return cls(deserialize_aws_json_1_1(data))
