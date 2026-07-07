"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#LimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.error_message


class LimitExceededException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.error_message.ErrorMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LimitExceededException_:
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class LimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisanalyticsv2#LimitExceededException``."""

    code: str | None = "LimitExceededException"

    def __init__(self, data: LimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "LimitExceededException":
        return cls(deserialize_aws_json_1_1(data))
