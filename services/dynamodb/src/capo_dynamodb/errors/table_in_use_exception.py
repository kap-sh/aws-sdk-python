"""Generated from Smithy shape ``com.amazonaws.dynamodb#TableInUseException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import capo_dynamodb.types.error_message


class TableInUseException_(TypedDict, closed=True):
    message: NotRequired["capo_dynamodb.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TableInUseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TableInUseException_:
    out: TableInUseException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class TableInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#TableInUseException``."""

    code: str | None = "TableInUseException"

    def __init__(self, data: TableInUseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TableInUseException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "TableInUseException":
        return cls(deserialize_aws_json_1_0(data))
