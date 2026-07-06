"""Generated from Smithy shape ``com.amazonaws.workmail#TooManyTagsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workmail.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.string


class TooManyTagsException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_workmail.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TooManyTagsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TooManyTagsException_:
    out: TooManyTagsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class TooManyTagsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workmail#TooManyTagsException``."""

    code: str | None = "TooManyTagsException"

    def __init__(self, data: TooManyTagsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyTagsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "TooManyTagsException":
        return cls(deserialize_aws_json_1_1(data))
