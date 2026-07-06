"""Generated from Smithy shape ``com.amazonaws.directconnect#DirectConnectClientException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_direct_connect.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.error_message


class DirectConnectClientException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_direct_connect.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectConnectClientException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectConnectClientException_:
    out: DirectConnectClientException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DirectConnectClientException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.directconnect#DirectConnectClientException``."""

    code: str | None = "DirectConnectClientException"

    def __init__(self, data: DirectConnectClientException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DirectConnectClientException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DirectConnectClientException":
        return cls(deserialize_aws_json_1_1(data))
