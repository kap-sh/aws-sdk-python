"""Generated from Smithy shape ``com.amazonaws.swf#DefaultUndefinedFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_swf.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_swf.types.error_message


class DefaultUndefinedFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_swf.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DefaultUndefinedFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DefaultUndefinedFault_:
    out: DefaultUndefinedFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DefaultUndefinedFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.swf#DefaultUndefinedFault``."""

    code: str | None = "DefaultUndefinedFault"

    def __init__(self, data: DefaultUndefinedFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DefaultUndefinedFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "DefaultUndefinedFault":
        return cls(deserialize_aws_json_1_0(data))
