"""Generated from Smithy shape ``com.amazonaws.ssm#TotalSizeLimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class TotalSizeLimitExceededException_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TotalSizeLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TotalSizeLimitExceededException_:
    out: TotalSizeLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class TotalSizeLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#TotalSizeLimitExceededException``."""

    code: str | None = "TotalSizeLimitExceededException"

    def __init__(self, data: TotalSizeLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TotalSizeLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "TotalSizeLimitExceededException":
        return cls(deserialize_aws_json_1_1(data))
