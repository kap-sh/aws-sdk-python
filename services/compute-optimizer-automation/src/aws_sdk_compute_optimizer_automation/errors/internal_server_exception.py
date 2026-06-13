"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#InternalServerException``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_compute_optimizer_automation.errors import ServiceError


class InternalServerException_(TypedDict):
    message: NotRequired["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InternalServerException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.computeoptimizerautomation#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(self, data: InternalServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "InternalServerException":
        return cls(deserialize_aws_json_1_0(data))
