"""Generated from Smithy shape ``com.amazonaws.mediastore#CorsPolicyNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mediastore.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.error_message


class CorsPolicyNotFoundException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_mediastore.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CorsPolicyNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CorsPolicyNotFoundException_:
    out: CorsPolicyNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class CorsPolicyNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediastore#CorsPolicyNotFoundException``."""

    code: str | None = "CorsPolicyNotFoundException"

    def __init__(self, data: CorsPolicyNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CorsPolicyNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "CorsPolicyNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
