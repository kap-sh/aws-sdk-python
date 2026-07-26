"""Generated from Smithy shape ``com.amazonaws.acm#TagPolicyException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_acm.errors import ServiceError

if TYPE_CHECKING:
    import capo_acm.types.string


class TagPolicyException_(TypedDict, closed=True):
    message: NotRequired["capo_acm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagPolicyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TagPolicyException_:
    out: TagPolicyException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class TagPolicyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.acm#TagPolicyException``."""

    code: str | None = "TagPolicyException"

    def __init__(self, data: TagPolicyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TagPolicyException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "TagPolicyException":
        return cls(deserialize_aws_json_1_1(data))
