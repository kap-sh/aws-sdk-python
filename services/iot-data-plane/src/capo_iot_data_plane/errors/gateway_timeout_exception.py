"""Generated from Smithy shape ``com.amazonaws.iotdataplane#GatewayTimeoutException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot_data_plane.errors import ServiceError

if TYPE_CHECKING:
    import capo_iot_data_plane.types.error_message


class GatewayTimeoutException_(TypedDict, closed=True):
    message: NotRequired["capo_iot_data_plane.types.error_message.errorMessage"]
    """<p>The message for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayTimeoutException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> GatewayTimeoutException_:
    out: GatewayTimeoutException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class GatewayTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotdataplane#GatewayTimeoutException``."""

    code: str | None = "GatewayTimeoutException"

    def __init__(self, data: GatewayTimeoutException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="GatewayTimeoutException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "GatewayTimeoutException":
        return cls(deserialize_json(data))
