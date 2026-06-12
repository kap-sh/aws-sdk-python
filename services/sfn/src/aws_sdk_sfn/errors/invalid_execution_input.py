"""Generated from Smithy shape ``com.amazonaws.sfn#InvalidExecutionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.error_message


class InvalidExecutionInput_(TypedDict):
    message: NotRequired["aws_sdk_sfn.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidExecutionInput_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvalidExecutionInput_:
    out: InvalidExecutionInput_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidExecutionInput(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sfn#InvalidExecutionInput``."""

    code: str | None = "InvalidExecutionInput"

    def __init__(self, data: InvalidExecutionInput_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidExecutionInput",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "InvalidExecutionInput":
        return cls(deserialize_aws_json_1_0(data))
