"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#ServiceLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudcontrol.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudcontrol.types.error_message


class ServiceLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudcontrol.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceLimitExceededException_:
    out: ServiceLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ServiceLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudcontrol#ServiceLimitExceededException``."""

    code: str | None = "ServiceLimitExceededException"

    def __init__(self, data: ServiceLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ServiceLimitExceededException":
        return cls(deserialize_aws_json_1_0(data))
