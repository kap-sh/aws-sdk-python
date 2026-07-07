"""Generated from Smithy shape ``com.amazonaws.swf#TooManyTagsFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_swf.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_swf.types.error_message


class TooManyTagsFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_swf.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TooManyTagsFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TooManyTagsFault_:
    out: TooManyTagsFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class TooManyTagsFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.swf#TooManyTagsFault``."""

    code: str | None = "TooManyTagsFault"

    def __init__(self, data: TooManyTagsFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyTagsFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "TooManyTagsFault":
        return cls(deserialize_aws_json_1_0(data))
