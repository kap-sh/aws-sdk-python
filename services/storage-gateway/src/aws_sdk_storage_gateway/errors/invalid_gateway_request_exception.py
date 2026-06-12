"""Generated from Smithy shape ``com.amazonaws.storagegateway#InvalidGatewayRequestException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_storage_gateway.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.storage_gateway_error
    import aws_sdk_storage_gateway.types.string


class InvalidGatewayRequestException_(TypedDict):
    message: NotRequired["aws_sdk_storage_gateway.types.string.string"]
    """<p>A human-readable message describing the error that occurred.</p>"""
    error: NotRequired[
        "aws_sdk_storage_gateway.types.storage_gateway_error.StorageGatewayError"
    ]
    """<p>A <a>StorageGatewayError</a> that provides more detail about the cause of the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidGatewayRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "error" in value:
        import aws_sdk_storage_gateway.types.storage_gateway_error

        out["error"] = (
            aws_sdk_storage_gateway.types.storage_gateway_error.serialize_aws_json_1_1(
                value["error"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidGatewayRequestException_:
    out: InvalidGatewayRequestException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "error" in data:
        import aws_sdk_storage_gateway.types.storage_gateway_error

        out["error"] = (
            aws_sdk_storage_gateway.types.storage_gateway_error.deserialize_aws_json_1_1(
                data["error"]
            )
        )
    return out


class InvalidGatewayRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.storagegateway#InvalidGatewayRequestException``."""

    code: str | None = "InvalidGatewayRequestException"

    def __init__(self, data: InvalidGatewayRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidGatewayRequestException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidGatewayRequestException":
        return cls(deserialize_aws_json_1_1(data))
