"""Generated from Smithy shape ``com.amazonaws.fsx#MissingFileCacheConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_fsx.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_fsx.types.error_message


class MissingFileCacheConfiguration_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MissingFileCacheConfiguration_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MissingFileCacheConfiguration_:
    out: MissingFileCacheConfiguration_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class MissingFileCacheConfiguration(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#MissingFileCacheConfiguration``."""

    code: str | None = "MissingFileCacheConfiguration"

    def __init__(self, data: MissingFileCacheConfiguration_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MissingFileCacheConfiguration",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "MissingFileCacheConfiguration":
        return cls(deserialize_aws_json_1_1(data))
