"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#AcceleratorNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_global_accelerator.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.error_message


class AcceleratorNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_global_accelerator.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceleratorNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AcceleratorNotFoundException_:
    out: AcceleratorNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AcceleratorNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.globalaccelerator#AcceleratorNotFoundException``."""

    code: str | None = "AcceleratorNotFoundException"

    def __init__(self, data: AcceleratorNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AcceleratorNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AcceleratorNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
