"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryTaskExecuting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_fsx.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_fsx.types.error_message


class DataRepositoryTaskExecuting_(TypedDict):
    message: NotRequired["aws_sdk_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataRepositoryTaskExecuting_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataRepositoryTaskExecuting_:
    out: DataRepositoryTaskExecuting_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DataRepositoryTaskExecuting(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#DataRepositoryTaskExecuting``."""

    code: str | None = "DataRepositoryTaskExecuting"

    def __init__(self, data: DataRepositoryTaskExecuting_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DataRepositoryTaskExecuting",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DataRepositoryTaskExecuting":
        return cls(deserialize_aws_json_1_1(data))
