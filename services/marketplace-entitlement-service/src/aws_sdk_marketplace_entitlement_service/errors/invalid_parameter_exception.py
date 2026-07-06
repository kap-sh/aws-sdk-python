"""Generated from Smithy shape ``com.amazonaws.marketplaceentitlementservice#InvalidParameterException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_entitlement_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_marketplace_entitlement_service.types.error_message


class InvalidParameterException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_marketplace_entitlement_service.types.error_message.ErrorMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidParameterException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidParameterException_:
    out: InvalidParameterException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplaceentitlementservice#InvalidParameterException``."""

    code: str | None = "InvalidParameterException"

    def __init__(self, data: InvalidParameterException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidParameterException":
        return cls(deserialize_aws_json_1_1(data))
