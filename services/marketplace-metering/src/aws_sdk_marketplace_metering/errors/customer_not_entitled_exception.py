"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#CustomerNotEntitledException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_marketplace_metering.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_marketplace_metering.types.error_message


class CustomerNotEntitledException_(TypedDict):
    message: NotRequired[
        "aws_sdk_marketplace_metering.types.error_message.errorMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomerNotEntitledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomerNotEntitledException_:
    out: CustomerNotEntitledException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class CustomerNotEntitledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplacemetering#CustomerNotEntitledException``."""

    code: str | None = "CustomerNotEntitledException"

    def __init__(self, data: CustomerNotEntitledException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CustomerNotEntitledException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "CustomerNotEntitledException":
        return cls(deserialize_aws_json_1_1(data))
