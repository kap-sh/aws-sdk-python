"""Generated from Smithy shape ``com.amazonaws.costexplorer#BackfillLimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cost_explorer.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.error_message


class BackfillLimitExceededException_(TypedDict):
    message: NotRequired["aws_sdk_cost_explorer.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BackfillLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BackfillLimitExceededException_:
    out: BackfillLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class BackfillLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.costexplorer#BackfillLimitExceededException``."""

    code: str | None = "BackfillLimitExceededException"

    def __init__(self, data: BackfillLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BackfillLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "BackfillLimitExceededException":
        return cls(deserialize_aws_json_1_1(data))
