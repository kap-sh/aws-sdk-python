"""Generated from Smithy shape ``com.amazonaws.ecr#LifecyclePolicyPreviewNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.exception_message


class LifecyclePolicyPreviewNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_ecr.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LifecyclePolicyPreviewNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LifecyclePolicyPreviewNotFoundException_:
    out: LifecyclePolicyPreviewNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class LifecyclePolicyPreviewNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#LifecyclePolicyPreviewNotFoundException``."""

    code: str | None = "LifecyclePolicyPreviewNotFoundException"

    def __init__(self, data: LifecyclePolicyPreviewNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LifecyclePolicyPreviewNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "LifecyclePolicyPreviewNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
