"""Generated from Smithy shape ``com.amazonaws.networkfirewall#InvalidResourcePolicyException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_firewall.errors import ServiceError

if TYPE_CHECKING:
    import capo_network_firewall.types.error_message


class InvalidResourcePolicyException_(TypedDict, closed=True):
    message: NotRequired["capo_network_firewall.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidResourcePolicyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvalidResourcePolicyException_:
    out: InvalidResourcePolicyException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidResourcePolicyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.networkfirewall#InvalidResourcePolicyException``."""

    code: str | None = "InvalidResourcePolicyException"

    def __init__(self, data: InvalidResourcePolicyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidResourcePolicyException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "InvalidResourcePolicyException":
        return cls(deserialize_aws_json_1_0(data))
