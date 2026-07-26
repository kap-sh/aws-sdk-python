"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTableAlreadyExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import capo_dynamodb.types.error_message


class GlobalTableAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["capo_dynamodb.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalTableAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GlobalTableAlreadyExistsException_:
    out: GlobalTableAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class GlobalTableAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#GlobalTableAlreadyExistsException``."""

    code: str | None = "GlobalTableAlreadyExistsException"

    def __init__(self, data: GlobalTableAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="GlobalTableAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "GlobalTableAlreadyExistsException":
        return cls(deserialize_aws_json_1_0(data))
