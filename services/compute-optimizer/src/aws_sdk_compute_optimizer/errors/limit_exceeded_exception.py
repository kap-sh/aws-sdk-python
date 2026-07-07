"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_compute_optimizer.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.error_message


class LimitExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_compute_optimizer.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LimitExceededException_:
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class LimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.computeoptimizer#LimitExceededException``."""

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
    def from_aws_json_1_0(cls, data: dict) -> "LimitExceededException":
        return cls(deserialize_aws_json_1_0(data))
