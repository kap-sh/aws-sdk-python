"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class OpsItemConflictException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemConflictException_:
    out: OpsItemConflictException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class OpsItemConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#OpsItemConflictException``."""

    code: str | None = "OpsItemConflictException"

    def __init__(self, data: OpsItemConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OpsItemConflictException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "OpsItemConflictException":
        return cls(deserialize_aws_json_1_1(data))
