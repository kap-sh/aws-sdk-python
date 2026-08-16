"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#InternalServerException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.message


class InternalServerException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudwatch_logs.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalServerException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatchlogs#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(self, data: InternalServerException_, message: str | None = None):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None
    ) -> "InternalServerException":
        return cls(deserialize_aws_json_1_1(data), message)
