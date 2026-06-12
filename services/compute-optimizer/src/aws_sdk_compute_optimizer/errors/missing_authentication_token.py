"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#MissingAuthenticationToken``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_compute_optimizer.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.error_message


class MissingAuthenticationToken_(TypedDict):
    message: NotRequired["aws_sdk_compute_optimizer.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MissingAuthenticationToken_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MissingAuthenticationToken_:
    out: MissingAuthenticationToken_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class MissingAuthenticationToken(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.computeoptimizer#MissingAuthenticationToken``."""

    code: str | None = "MissingAuthenticationToken"

    def __init__(self, data: MissingAuthenticationToken_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MissingAuthenticationToken",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "MissingAuthenticationToken":
        return cls(deserialize_aws_json_1_0(data))
