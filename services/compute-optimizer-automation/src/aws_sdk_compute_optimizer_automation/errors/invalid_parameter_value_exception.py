"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#InvalidParameterValueException``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_compute_optimizer_automation.errors import ServiceError


class InvalidParameterValueException_(TypedDict):
    message: NotRequired["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidParameterValueException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvalidParameterValueException_:
    out: InvalidParameterValueException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidParameterValueException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.computeoptimizerautomation#InvalidParameterValueException``."""

    code: str | None = "InvalidParameterValueException"

    def __init__(self, data: InvalidParameterValueException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterValueException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "InvalidParameterValueException":
        return cls(deserialize_aws_json_1_0(data))
