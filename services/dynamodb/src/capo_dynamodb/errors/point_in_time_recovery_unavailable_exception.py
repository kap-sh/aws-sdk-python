"""Generated from Smithy shape ``com.amazonaws.dynamodb#PointInTimeRecoveryUnavailableException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import capo_dynamodb.types.error_message


class PointInTimeRecoveryUnavailableException_(TypedDict, closed=True):
    message: NotRequired["capo_dynamodb.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PointInTimeRecoveryUnavailableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PointInTimeRecoveryUnavailableException_:
    out: PointInTimeRecoveryUnavailableException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class PointInTimeRecoveryUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#PointInTimeRecoveryUnavailableException``."""

    code: str | None = "PointInTimeRecoveryUnavailableException"

    def __init__(self, data: PointInTimeRecoveryUnavailableException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PointInTimeRecoveryUnavailableException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "PointInTimeRecoveryUnavailableException":
        return cls(deserialize_aws_json_1_0(data))
