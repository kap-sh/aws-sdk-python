"""Generated from Smithy shape ``com.amazonaws.ecr#UnableToGetUpstreamLayerException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecr.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.exception_message


class UnableToGetUpstreamLayerException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ecr.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnableToGetUpstreamLayerException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnableToGetUpstreamLayerException_:
    out: UnableToGetUpstreamLayerException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnableToGetUpstreamLayerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#UnableToGetUpstreamLayerException``."""

    code: str | None = "UnableToGetUpstreamLayerException"

    def __init__(self, data: UnableToGetUpstreamLayerException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnableToGetUpstreamLayerException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnableToGetUpstreamLayerException":
        return cls(deserialize_aws_json_1_1(data))
