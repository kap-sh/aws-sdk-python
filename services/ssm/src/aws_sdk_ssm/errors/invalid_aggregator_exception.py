"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidAggregatorException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class InvalidAggregatorException_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidAggregatorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidAggregatorException_:
    out: InvalidAggregatorException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidAggregatorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidAggregatorException``."""

    code: str | None = "InvalidAggregatorException"

    def __init__(self, data: InvalidAggregatorException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidAggregatorException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidAggregatorException":
        return cls(deserialize_aws_json_1_1(data))
