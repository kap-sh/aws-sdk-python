"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidActivation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class InvalidActivation_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidActivation_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidActivation_:
    out: InvalidActivation_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidActivation(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidActivation``."""

    code: str | None = "InvalidActivation"

    def __init__(self, data: InvalidActivation_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidActivation",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidActivation":
        return cls(deserialize_aws_json_1_1(data))
