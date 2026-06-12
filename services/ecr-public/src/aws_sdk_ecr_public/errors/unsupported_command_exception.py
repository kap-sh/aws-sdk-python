"""Generated from Smithy shape ``com.amazonaws.ecrpublic#UnsupportedCommandException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr_public.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.exception_message


class UnsupportedCommandException_(TypedDict):
    message: NotRequired["aws_sdk_ecr_public.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedCommandException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedCommandException_:
    out: UnsupportedCommandException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnsupportedCommandException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecrpublic#UnsupportedCommandException``."""

    code: str | None = "UnsupportedCommandException"

    def __init__(self, data: UnsupportedCommandException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedCommandException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnsupportedCommandException":
        return cls(deserialize_aws_json_1_1(data))
