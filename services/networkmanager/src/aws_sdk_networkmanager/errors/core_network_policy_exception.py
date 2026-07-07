"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkPolicyException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_networkmanager.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network_policy_error_list
    import aws_sdk_networkmanager.types.server_side_string


class CoreNetworkPolicyException_(TypedDict, closed=True):
    message: "aws_sdk_networkmanager.types.server_side_string.ServerSideString"
    errors: NotRequired[
        "aws_sdk_networkmanager.types.core_network_policy_error_list.CoreNetworkPolicyErrorList"
    ]
    """<p>Describes a core network policy exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkPolicyException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "errors" in value:
        import aws_sdk_networkmanager.types.core_network_policy_error_list

        out["Errors"] = (
            aws_sdk_networkmanager.types.core_network_policy_error_list.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoreNetworkPolicyException_:
    out: CoreNetworkPolicyException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("CoreNetworkPolicyException_.message required")
    if "Errors" in data:
        import aws_sdk_networkmanager.types.core_network_policy_error_list

        out["errors"] = (
            aws_sdk_networkmanager.types.core_network_policy_error_list.deserialize_json(
                data["Errors"]
            )
        )
    return out


class CoreNetworkPolicyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.networkmanager#CoreNetworkPolicyException``."""

    code: str | None = "CoreNetworkPolicyException"

    def __init__(self, data: CoreNetworkPolicyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CoreNetworkPolicyException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "CoreNetworkPolicyException":
        return cls(deserialize_json(data))
