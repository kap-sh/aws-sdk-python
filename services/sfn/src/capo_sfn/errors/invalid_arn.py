"""Generated from Smithy shape ``com.amazonaws.sfn#InvalidArn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import ServiceError

if TYPE_CHECKING:
    import capo_sfn.types.error_message


class InvalidArn_(TypedDict, closed=True):
    message: NotRequired["capo_sfn.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidArn_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvalidArn_:
    out: InvalidArn_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidArn(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sfn#InvalidArn``."""

    code: str | None = "InvalidArn"

    def __init__(self, data: InvalidArn_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidArn",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict, message: str | None = None) -> "InvalidArn":
        return cls(deserialize_aws_json_1_0(data), message)
