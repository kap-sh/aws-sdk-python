"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryTaskNotFound``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fsx.errors import ServiceError

if TYPE_CHECKING:
    import capo_fsx.types.error_message


class DataRepositoryTaskNotFound_(TypedDict, closed=True):
    message: NotRequired["capo_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataRepositoryTaskNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataRepositoryTaskNotFound_:
    out: DataRepositoryTaskNotFound_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DataRepositoryTaskNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#DataRepositoryTaskNotFound``."""

    code: str | None = "DataRepositoryTaskNotFound"

    def __init__(self, data: DataRepositoryTaskNotFound_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DataRepositoryTaskNotFound",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DataRepositoryTaskNotFound":
        return cls(deserialize_aws_json_1_1(data))
