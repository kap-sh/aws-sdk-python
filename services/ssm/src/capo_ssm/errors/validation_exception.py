"""Generated from Smithy shape ``com.amazonaws.ssm#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class ValidationException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]
    reason_code: NotRequired["capo_ssm.types.string.String"]
    """<p>The reason code for the invalid request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason_code" in value:
        out["ReasonCode"] = value["reason_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ReasonCode" in data:
        out["reason_code"] = data["ReasonCode"]
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(self, data: ValidationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ValidationException":
        return cls(deserialize_aws_json_1_1(data))
