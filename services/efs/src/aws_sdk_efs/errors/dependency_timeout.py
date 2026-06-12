"""Generated from Smithy shape ``com.amazonaws.efs#DependencyTimeout``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_efs.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_efs.types.error_code
    import aws_sdk_efs.types.error_message


class DependencyTimeout_(TypedDict):
    error_code: "aws_sdk_efs.types.error_code.ErrorCode"
    message: NotRequired["aws_sdk_efs.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: DependencyTimeout_) -> dict:
    out: dict = {}
    out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DependencyTimeout_:
    out: DependencyTimeout_ = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    else:
        raise DeserializationError("DependencyTimeout_.error_code required")
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DependencyTimeout(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.efs#DependencyTimeout``."""

    code: str | None = "DependencyTimeout"

    def __init__(self, data: DependencyTimeout_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="DependencyTimeout",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DependencyTimeout":
        return cls(deserialize_json(data))
