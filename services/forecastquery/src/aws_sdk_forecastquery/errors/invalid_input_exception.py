"""Generated from Smithy shape ``com.amazonaws.forecastquery#InvalidInputException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_forecastquery.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_forecastquery.types.error_message


class InvalidInputException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_forecastquery.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidInputException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidInputException_:
    out: InvalidInputException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidInputException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.forecastquery#InvalidInputException``."""

    code: str | None = "InvalidInputException"

    def __init__(self, data: InvalidInputException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidInputException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidInputException":
        return cls(deserialize_aws_json_1_1(data))
