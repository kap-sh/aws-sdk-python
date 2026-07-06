"""Generated from Smithy shape ``com.amazonaws.budgets#DuplicateRecordException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_budgets.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.error_message


class DuplicateRecordException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_budgets.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DuplicateRecordException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DuplicateRecordException_:
    out: DuplicateRecordException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DuplicateRecordException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.budgets#DuplicateRecordException``."""

    code: str | None = "DuplicateRecordException"

    def __init__(self, data: DuplicateRecordException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicateRecordException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DuplicateRecordException":
        return cls(deserialize_aws_json_1_1(data))
