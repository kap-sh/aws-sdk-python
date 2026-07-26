"""Generated from Smithy shape ``com.amazonaws.billing#BillingViewHealthStatusException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_billing.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_billing.types.error_message


class BillingViewHealthStatusException_(TypedDict, closed=True):
    message: "capo_billing.types.error_message.ErrorMessage"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingViewHealthStatusException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BillingViewHealthStatusException_:
    out: BillingViewHealthStatusException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("BillingViewHealthStatusException_.message required")
    return out


class BillingViewHealthStatusException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.billing#BillingViewHealthStatusException``."""

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
    def from_aws_json_1_0(cls, data: dict) -> "BillingViewHealthStatusException":
        return cls(deserialize_aws_json_1_0(data))
