"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ServiceAttributesLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_servicediscovery.errors import ServiceError

if TYPE_CHECKING:
    import capo_servicediscovery.types.error_message


class ServiceAttributesLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_servicediscovery.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceAttributesLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceAttributesLimitExceededException_:
    out: ServiceAttributesLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ServiceAttributesLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicediscovery#ServiceAttributesLimitExceededException``."""

    code: str | None = "ServiceAttributesLimitExceededException"

    def __init__(self, data: ServiceAttributesLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceAttributesLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ServiceAttributesLimitExceededException":
        return cls(deserialize_aws_json_1_1(data))
