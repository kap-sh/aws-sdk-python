"""Generated from Smithy shape ``com.amazonaws.marketplaceentitlementservice#InternalServiceErrorException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_entitlement_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_marketplace_entitlement_service.types.error_message


class InternalServiceErrorException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_marketplace_entitlement_service.types.error_message.ErrorMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalServiceErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalServiceErrorException_:
    out: InternalServiceErrorException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InternalServiceErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplaceentitlementservice#InternalServiceErrorException``."""

    code: str | None = "InternalServiceErrorException"

    def __init__(self, data: InternalServiceErrorException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServiceErrorException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InternalServiceErrorException":
        return cls(deserialize_aws_json_1_1(data))
