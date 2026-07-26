"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicatedWriteConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import capo_dynamodb.types.error_message


class ReplicatedWriteConflictException_(TypedDict, closed=True):
    message: NotRequired["capo_dynamodb.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicatedWriteConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicatedWriteConflictException_:
    out: ReplicatedWriteConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ReplicatedWriteConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ReplicatedWriteConflictException``."""

    code: str | None = "ReplicatedWriteConflictException"

    def __init__(self, data: ReplicatedWriteConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="ReplicatedWriteConflictException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ReplicatedWriteConflictException":
        return cls(deserialize_aws_json_1_0(data))
