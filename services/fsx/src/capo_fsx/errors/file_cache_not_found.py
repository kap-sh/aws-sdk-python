"""Generated from Smithy shape ``com.amazonaws.fsx#FileCacheNotFound``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fsx.errors import ServiceError

if TYPE_CHECKING:
    import capo_fsx.types.error_message


class FileCacheNotFound_(TypedDict, closed=True):
    message: NotRequired["capo_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileCacheNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FileCacheNotFound_:
    out: FileCacheNotFound_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class FileCacheNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#FileCacheNotFound``."""

    code: str | None = "FileCacheNotFound"

    def __init__(self, data: FileCacheNotFound_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FileCacheNotFound",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "FileCacheNotFound":
        return cls(deserialize_aws_json_1_1(data))
