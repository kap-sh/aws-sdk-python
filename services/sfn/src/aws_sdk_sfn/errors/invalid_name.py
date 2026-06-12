"""Generated from Smithy shape ``com.amazonaws.sfn#InvalidName``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.error_message


class InvalidName_(TypedDict):
    message: NotRequired["aws_sdk_sfn.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidName_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvalidName_:
    out: InvalidName_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidName(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sfn#InvalidName``."""

    code: str | None = "InvalidName"

    def __init__(self, data: InvalidName_):
        super().__init__(
            "client", is_throttling_error=False, is_retryable=False, code="InvalidName"
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "InvalidName":
        return cls(deserialize_aws_json_1_0(data))
