"""Generated from Smithy shape ``com.amazonaws.codepipeline#InvalidArnException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codepipeline.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.message


class InvalidArnException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_codepipeline.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidArnException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidArnException_:
    out: InvalidArnException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidArnException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codepipeline#InvalidArnException``."""

    code: str | None = "InvalidArnException"

    def __init__(self, data: InvalidArnException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidArnException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidArnException":
        return cls(deserialize_aws_json_1_1(data))
