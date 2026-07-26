"""Generated from Smithy shape ``com.amazonaws.wafv2#WAFOptimisticLockException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import ServiceError

if TYPE_CHECKING:
    import capo_wafv2.types.error_message


class WAFOptimisticLockException_(TypedDict, closed=True):
    message: NotRequired["capo_wafv2.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFOptimisticLockException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFOptimisticLockException_:
    out: WAFOptimisticLockException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class WAFOptimisticLockException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafv2#WAFOptimisticLockException``."""

    code: str | None = "WAFOptimisticLockException"

    def __init__(self, data: WAFOptimisticLockException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFOptimisticLockException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "WAFOptimisticLockException":
        return cls(deserialize_aws_json_1_1(data))
