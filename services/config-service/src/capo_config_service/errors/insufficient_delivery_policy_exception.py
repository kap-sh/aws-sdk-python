"""Generated from Smithy shape ``com.amazonaws.configservice#InsufficientDeliveryPolicyException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_config_service.types.error_message


class InsufficientDeliveryPolicyException_(TypedDict, closed=True):
    message: NotRequired["capo_config_service.types.error_message.ErrorMessage"]
    """<p>Error executing the command</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InsufficientDeliveryPolicyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InsufficientDeliveryPolicyException_:
    out: InsufficientDeliveryPolicyException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InsufficientDeliveryPolicyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.configservice#InsufficientDeliveryPolicyException``."""

    code: str | None = "InsufficientDeliveryPolicyException"

    def __init__(self, data: InsufficientDeliveryPolicyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InsufficientDeliveryPolicyException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InsufficientDeliveryPolicyException":
        return cls(deserialize_aws_json_1_1(data))
