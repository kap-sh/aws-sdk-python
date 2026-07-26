"""Generated from Smithy shape ``com.amazonaws.machinelearning#InvalidInputException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_machine_learning.errors import ServiceError

if TYPE_CHECKING:
    import capo_machine_learning.types.error_code
    import capo_machine_learning.types.error_message


class InvalidInputException_(TypedDict, closed=True):
    message: NotRequired["capo_machine_learning.types.error_message.ErrorMessage"]
    code: "capo_machine_learning.types.error_code.ErrorCode"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidInputException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    out["code"] = value.get("code", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidInputException_:
    out: InvalidInputException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "code" in data:
        out["code"] = data["code"]
    else:
        out["code"] = 0
    return out


class InvalidInputException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.machinelearning#InvalidInputException``."""

    code: str | None = "InvalidInputException"

    def __init__(self, data: InvalidInputException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidInputException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidInputException":
        return cls(deserialize_aws_json_1_1(data))
