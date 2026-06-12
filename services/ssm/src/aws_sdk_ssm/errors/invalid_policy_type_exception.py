"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidPolicyTypeException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class InvalidPolicyTypeException_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidPolicyTypeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidPolicyTypeException_:
    out: InvalidPolicyTypeException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidPolicyTypeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidPolicyTypeException``."""

    code: str | None = "InvalidPolicyTypeException"

    def __init__(self, data: InvalidPolicyTypeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPolicyTypeException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidPolicyTypeException":
        return cls(deserialize_aws_json_1_1(data))
