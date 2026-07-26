"""Generated from Smithy shape ``com.amazonaws.migrationhub#PolicyErrorException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_migration_hub.errors import ServiceError

if TYPE_CHECKING:
    import capo_migration_hub.types.error_message


class PolicyErrorException_(TypedDict, closed=True):
    message: NotRequired["capo_migration_hub.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PolicyErrorException_:
    out: PolicyErrorException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class PolicyErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.migrationhub#PolicyErrorException``."""

    code: str | None = "PolicyErrorException"

    def __init__(self, data: PolicyErrorException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicyErrorException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "PolicyErrorException":
        return cls(deserialize_aws_json_1_1(data))
