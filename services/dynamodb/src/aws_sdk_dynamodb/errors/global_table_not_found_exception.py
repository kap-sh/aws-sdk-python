"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTableNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class GlobalTableNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalTableNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GlobalTableNotFoundException_:
    out: GlobalTableNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class GlobalTableNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#GlobalTableNotFoundException``."""

    code: str | None = "GlobalTableNotFoundException"

    def __init__(self, data: GlobalTableNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="GlobalTableNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "GlobalTableNotFoundException":
        return cls(deserialize_aws_json_1_0(data))
