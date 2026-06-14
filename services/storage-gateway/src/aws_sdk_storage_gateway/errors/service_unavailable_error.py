"""Generated from Smithy shape ``com.amazonaws.storagegateway#ServiceUnavailableError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_storage_gateway.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.storage_gateway_error
    import aws_sdk_storage_gateway.types.string


class ServiceUnavailableError_(TypedDict):
    message: NotRequired["aws_sdk_storage_gateway.types.string.string"]
    """<p>A human-readable message describing the error that occurred.</p>"""
    error: NotRequired[
        "aws_sdk_storage_gateway.types.storage_gateway_error.StorageGatewayError"
    ]
    """<p>A <a>StorageGatewayError</a> that provides more information about the cause of the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceUnavailableError_) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> ServiceUnavailableError_:
    out: ServiceUnavailableError_ = {}  # type: ignore[typeddict-item]
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


class ServiceUnavailableError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.storagegateway#ServiceUnavailableError``."""

    code: str | None = "ServiceUnavailableError"

    def __init__(self, data: ServiceUnavailableError_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceUnavailableError",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ServiceUnavailableError":
        return cls(deserialize_aws_json_1_1(data))
