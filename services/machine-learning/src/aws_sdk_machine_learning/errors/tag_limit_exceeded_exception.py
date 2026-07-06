"""Generated from Smithy shape ``com.amazonaws.machinelearning#TagLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_machine_learning.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.error_message


class TagLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_machine_learning.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TagLimitExceededException_:
    out: TagLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class TagLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.machinelearning#TagLimitExceededException``."""

    code: str | None = "TagLimitExceededException"

    def __init__(self, data: TagLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TagLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "TagLimitExceededException":
        return cls(deserialize_aws_json_1_1(data))
