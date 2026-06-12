"""Generated from Smithy shape ``com.amazonaws.kinesis#ExpiredNextTokenException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.error_message


class ExpiredNextTokenException_(TypedDict):
    message: NotRequired["aws_sdk_kinesis.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpiredNextTokenException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpiredNextTokenException_:
    out: ExpiredNextTokenException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ExpiredNextTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesis#ExpiredNextTokenException``."""

    code: str | None = "ExpiredNextTokenException"

    def __init__(self, data: ExpiredNextTokenException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ExpiredNextTokenException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ExpiredNextTokenException":
        return cls(deserialize_aws_json_1_1(data))
