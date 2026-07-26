"""Generated from Smithy shape ``com.amazonaws.budgets#BillingViewHealthStatusException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_budgets.errors import ServiceError

if TYPE_CHECKING:
    import capo_budgets.types.error_message


class BillingViewHealthStatusException_(TypedDict, closed=True):
    message: NotRequired["capo_budgets.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BillingViewHealthStatusException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BillingViewHealthStatusException_:
    out: BillingViewHealthStatusException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class BillingViewHealthStatusException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.budgets#BillingViewHealthStatusException``."""

    code: str | None = "BillingViewHealthStatusException"

    def __init__(self, data: BillingViewHealthStatusException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BillingViewHealthStatusException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "BillingViewHealthStatusException":
        return cls(deserialize_aws_json_1_1(data))
