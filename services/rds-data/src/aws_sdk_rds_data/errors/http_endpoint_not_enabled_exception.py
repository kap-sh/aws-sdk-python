"""Generated from Smithy shape ``com.amazonaws.rdsdata#HttpEndpointNotEnabledException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds_data.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.error_message


class HttpEndpointNotEnabledException_(TypedDict):
    message: NotRequired["aws_sdk_rds_data.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: HttpEndpointNotEnabledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> HttpEndpointNotEnabledException_:
    out: HttpEndpointNotEnabledException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class HttpEndpointNotEnabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rdsdata#HttpEndpointNotEnabledException``."""

    code: str | None = "HttpEndpointNotEnabledException"

    def __init__(self, data: HttpEndpointNotEnabledException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="HttpEndpointNotEnabledException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "HttpEndpointNotEnabledException":
        return cls(deserialize_json(data))
