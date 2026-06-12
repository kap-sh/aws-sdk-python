"""Generated from Smithy shape ``com.amazonaws.machinelearning#IdempotentParameterMismatchException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_machine_learning.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.error_code
    import aws_sdk_machine_learning.types.error_message


class IdempotentParameterMismatchException_(TypedDict):
    message: NotRequired["aws_sdk_machine_learning.types.error_message.ErrorMessage"]
    code: "aws_sdk_machine_learning.types.error_code.ErrorCode"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdempotentParameterMismatchException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    out["code"] = value.get("code", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> IdempotentParameterMismatchException_:
    out: IdempotentParameterMismatchException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "code" in data:
        out["code"] = data["code"]
    else:
        out["code"] = 0
    return out


class IdempotentParameterMismatchException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.machinelearning#IdempotentParameterMismatchException``."""

    code: str | None = "IdempotentParameterMismatchException"

    def __init__(self, data: IdempotentParameterMismatchException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IdempotentParameterMismatchException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "IdempotentParameterMismatchException":
        return cls(deserialize_aws_json_1_1(data))
