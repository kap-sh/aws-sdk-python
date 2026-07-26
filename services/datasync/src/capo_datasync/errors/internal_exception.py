"""Generated from Smithy shape ``com.amazonaws.datasync#InternalException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datasync.errors import ServiceError

if TYPE_CHECKING:
    import capo_datasync.types.string


class InternalException_(TypedDict, closed=True):
    message: NotRequired["capo_datasync.types.string.string"]
    error_code: NotRequired["capo_datasync.types.string.string"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalException_:
    out: InternalException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    return out


class InternalException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.datasync#InternalException``."""

    code: str | None = "InternalException"

    def __init__(self, data: InternalException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InternalException":
        return cls(deserialize_aws_json_1_1(data))
