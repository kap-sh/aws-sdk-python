"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#RequestTokenNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudcontrol.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudcontrol.types.error_message


class RequestTokenNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_cloudcontrol.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RequestTokenNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RequestTokenNotFoundException_:
    out: RequestTokenNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class RequestTokenNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudcontrol#RequestTokenNotFoundException``."""

    code: str | None = "RequestTokenNotFoundException"

    def __init__(self, data: RequestTokenNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RequestTokenNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "RequestTokenNotFoundException":
        return cls(deserialize_aws_json_1_0(data))
