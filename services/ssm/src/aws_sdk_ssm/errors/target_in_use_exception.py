"""Generated from Smithy shape ``com.amazonaws.ssm#TargetInUseException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class TargetInUseException_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetInUseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetInUseException_:
    out: TargetInUseException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class TargetInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#TargetInUseException``."""

    code: str | None = "TargetInUseException"

    def __init__(self, data: TargetInUseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TargetInUseException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "TargetInUseException":
        return cls(deserialize_aws_json_1_1(data))
