"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ByoipCidrNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_global_accelerator.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.error_message


class ByoipCidrNotFoundException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_global_accelerator.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ByoipCidrNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ByoipCidrNotFoundException_:
    out: ByoipCidrNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ByoipCidrNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.globalaccelerator#ByoipCidrNotFoundException``."""

    code: str | None = "ByoipCidrNotFoundException"

    def __init__(self, data: ByoipCidrNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ByoipCidrNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ByoipCidrNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
