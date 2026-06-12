"""Generated from Smithy shape ``com.amazonaws.fsx#AccessPointAlreadyOwnedByYou``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_fsx.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_fsx.types.error_code
    import aws_sdk_fsx.types.error_message


class AccessPointAlreadyOwnedByYou_(TypedDict):
    error_code: NotRequired["aws_sdk_fsx.types.error_code.ErrorCode"]
    """<p>An error code indicating that an access point with that name already exists in the Amazon Web Services Region in your Amazon Web Services account.</p>"""
    message: NotRequired["aws_sdk_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessPointAlreadyOwnedByYou_) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessPointAlreadyOwnedByYou_:
    out: AccessPointAlreadyOwnedByYou_ = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AccessPointAlreadyOwnedByYou(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#AccessPointAlreadyOwnedByYou``."""

    code: str | None = "AccessPointAlreadyOwnedByYou"

    def __init__(self, data: AccessPointAlreadyOwnedByYou_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessPointAlreadyOwnedByYou",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AccessPointAlreadyOwnedByYou":
        return cls(deserialize_aws_json_1_1(data))
