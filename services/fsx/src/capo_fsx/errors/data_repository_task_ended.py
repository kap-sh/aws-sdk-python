"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryTaskEnded``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fsx.errors import ServiceError

if TYPE_CHECKING:
    import capo_fsx.types.error_message


class DataRepositoryTaskEnded_(TypedDict, closed=True):
    message: NotRequired["capo_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataRepositoryTaskEnded_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataRepositoryTaskEnded_:
    out: DataRepositoryTaskEnded_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DataRepositoryTaskEnded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#DataRepositoryTaskEnded``."""

    code: str | None = "DataRepositoryTaskEnded"

    def __init__(self, data: DataRepositoryTaskEnded_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DataRepositoryTaskEnded",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DataRepositoryTaskEnded":
        return cls(deserialize_aws_json_1_1(data))
