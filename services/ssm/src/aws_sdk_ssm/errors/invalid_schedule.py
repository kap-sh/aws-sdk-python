"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidSchedule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class InvalidSchedule_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidSchedule_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidSchedule_:
    out: InvalidSchedule_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidSchedule(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidSchedule``."""

    code: str | None = "InvalidSchedule"

    def __init__(self, data: InvalidSchedule_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidSchedule",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidSchedule":
        return cls(deserialize_aws_json_1_1(data))
