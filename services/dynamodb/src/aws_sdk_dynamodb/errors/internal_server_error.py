"""Generated from Smithy shape ``com.amazonaws.dynamodb#InternalServerError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class InternalServerError_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]
    """<p>The server encountered an internal error trying to fulfill the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InternalServerError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InternalServerError_:
    out: InternalServerError_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InternalServerError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#InternalServerError``."""

    code: str | None = "InternalServerError"

    def __init__(self, data: InternalServerError_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerError",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "InternalServerError":
        return cls(deserialize_aws_json_1_0(data))
