"""Generated from Smithy shape ``com.amazonaws.dynamodb#PolicyNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class PolicyNotFoundException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PolicyNotFoundException_:
    out: PolicyNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class PolicyNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#PolicyNotFoundException``."""

    code: str | None = "PolicyNotFoundException"

    def __init__(self, data: PolicyNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicyNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "PolicyNotFoundException":
        return cls(deserialize_aws_json_1_0(data))
