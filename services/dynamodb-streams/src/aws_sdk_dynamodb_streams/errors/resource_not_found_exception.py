"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dynamodb_streams.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb_streams.types.error_message


class ResourceNotFoundException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_dynamodb_streams.types.error_message.ErrorMessage"]
    """<p>The resource which is being requested does not exist.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodbstreams#ResourceNotFoundException``."""

    code: str | None = "ResourceNotFoundException"

    def __init__(self, data: ResourceNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ResourceNotFoundException":
        return cls(deserialize_aws_json_1_0(data))
