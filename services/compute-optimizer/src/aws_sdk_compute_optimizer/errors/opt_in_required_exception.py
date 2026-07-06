"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#OptInRequiredException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_compute_optimizer.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.error_message


class OptInRequiredException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_compute_optimizer.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OptInRequiredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> OptInRequiredException_:
    out: OptInRequiredException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class OptInRequiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.computeoptimizer#OptInRequiredException``."""

    code: str | None = "OptInRequiredException"

    def __init__(self, data: OptInRequiredException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OptInRequiredException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "OptInRequiredException":
        return cls(deserialize_aws_json_1_0(data))
