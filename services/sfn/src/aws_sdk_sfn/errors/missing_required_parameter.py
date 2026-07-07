"""Generated from Smithy shape ``com.amazonaws.sfn#MissingRequiredParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sfn.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.error_message


class MissingRequiredParameter_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_sfn.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MissingRequiredParameter_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MissingRequiredParameter_:
    out: MissingRequiredParameter_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class MissingRequiredParameter(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sfn#MissingRequiredParameter``."""

    code: str | None = "MissingRequiredParameter"

    def __init__(self, data: MissingRequiredParameter_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MissingRequiredParameter",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "MissingRequiredParameter":
        return cls(deserialize_aws_json_1_0(data))
