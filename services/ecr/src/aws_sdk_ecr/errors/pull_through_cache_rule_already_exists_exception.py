"""Generated from Smithy shape ``com.amazonaws.ecr#PullThroughCacheRuleAlreadyExistsException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.exception_message


class PullThroughCacheRuleAlreadyExistsException_(TypedDict):
    message: NotRequired["aws_sdk_ecr.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullThroughCacheRuleAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PullThroughCacheRuleAlreadyExistsException_:
    out: PullThroughCacheRuleAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class PullThroughCacheRuleAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#PullThroughCacheRuleAlreadyExistsException``."""

    code: str | None = "PullThroughCacheRuleAlreadyExistsException"

    def __init__(self, data: PullThroughCacheRuleAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PullThroughCacheRuleAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "PullThroughCacheRuleAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data))
