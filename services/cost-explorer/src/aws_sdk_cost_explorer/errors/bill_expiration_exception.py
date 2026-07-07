"""Generated from Smithy shape ``com.amazonaws.costexplorer#BillExpirationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cost_explorer.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.error_message


class BillExpirationException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cost_explorer.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BillExpirationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BillExpirationException_:
    out: BillExpirationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class BillExpirationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.costexplorer#BillExpirationException``."""

    code: str | None = "BillExpirationException"

    def __init__(self, data: BillExpirationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BillExpirationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "BillExpirationException":
        return cls(deserialize_aws_json_1_1(data))
