"""Generated from Smithy shape ``com.amazonaws.fsx#BadRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_fsx.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_fsx.types.error_message


class BadRequest_(TypedDict):
    message: NotRequired["aws_sdk_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BadRequest_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BadRequest_:
    out: BadRequest_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class BadRequest(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#BadRequest``."""

    code: str | None = "BadRequest"

    def __init__(self, data: BadRequest_):
        super().__init__(
            "client", is_throttling_error=False, is_retryable=False, code="BadRequest"
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "BadRequest":
        return cls(deserialize_aws_json_1_1(data))
