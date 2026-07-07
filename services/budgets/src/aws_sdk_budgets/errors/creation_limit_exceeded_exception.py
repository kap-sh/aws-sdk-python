"""Generated from Smithy shape ``com.amazonaws.budgets#CreationLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_budgets.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.error_message


class CreationLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_budgets.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreationLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreationLimitExceededException_:
    out: CreationLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class CreationLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.budgets#CreationLimitExceededException``."""

    code: str | None = "CreationLimitExceededException"

    def __init__(self, data: CreationLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CreationLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "CreationLimitExceededException":
        return cls(deserialize_aws_json_1_1(data))
