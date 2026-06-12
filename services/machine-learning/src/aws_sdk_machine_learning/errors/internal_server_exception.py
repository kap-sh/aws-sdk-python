"""Generated from Smithy shape ``com.amazonaws.machinelearning#InternalServerException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_machine_learning.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.error_code
    import aws_sdk_machine_learning.types.error_message


class InternalServerException_(TypedDict):
    message: NotRequired["aws_sdk_machine_learning.types.error_message.ErrorMessage"]
    code: "aws_sdk_machine_learning.types.error_code.ErrorCode"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalServerException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    out["code"] = value.get("code", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "code" in data:
        out["code"] = data["code"]
    else:
        out["code"] = 0
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.machinelearning#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(self, data: InternalServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InternalServerException":
        return cls(deserialize_aws_json_1_1(data))
