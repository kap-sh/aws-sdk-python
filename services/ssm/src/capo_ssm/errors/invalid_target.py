"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class InvalidTarget_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidTarget_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidTarget_:
    out: InvalidTarget_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidTarget(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidTarget``."""

    code: str | None = "InvalidTarget"

    def __init__(self, data: InvalidTarget_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidTarget",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidTarget":
        return cls(deserialize_aws_json_1_1(data))
