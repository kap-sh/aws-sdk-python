"""Generated from Smithy shape ``com.amazonaws.ecr#UnableToGetUpstreamImageException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.exception_message


class UnableToGetUpstreamImageException_(TypedDict):
    message: NotRequired["aws_sdk_ecr.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnableToGetUpstreamImageException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnableToGetUpstreamImageException_:
    out: UnableToGetUpstreamImageException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnableToGetUpstreamImageException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#UnableToGetUpstreamImageException``."""

    code: str | None = "UnableToGetUpstreamImageException"

    def __init__(self, data: UnableToGetUpstreamImageException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnableToGetUpstreamImageException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnableToGetUpstreamImageException":
        return cls(deserialize_aws_json_1_1(data))
