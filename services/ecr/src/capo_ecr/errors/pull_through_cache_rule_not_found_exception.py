"""Generated from Smithy shape ``com.amazonaws.ecr#PullThroughCacheRuleNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecr.errors import ServiceError

if TYPE_CHECKING:
    import capo_ecr.types.exception_message


class PullThroughCacheRuleNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_ecr.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullThroughCacheRuleNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PullThroughCacheRuleNotFoundException_:
    out: PullThroughCacheRuleNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class PullThroughCacheRuleNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#PullThroughCacheRuleNotFoundException``."""

    code: str | None = "PullThroughCacheRuleNotFoundException"

    def __init__(self, data: PullThroughCacheRuleNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PullThroughCacheRuleNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "PullThroughCacheRuleNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
