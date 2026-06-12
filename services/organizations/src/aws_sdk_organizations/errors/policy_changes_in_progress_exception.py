"""Generated from Smithy shape ``com.amazonaws.organizations#PolicyChangesInProgressException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_organizations.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.exception_message


class PolicyChangesInProgressException_(TypedDict):
    message: NotRequired[
        "aws_sdk_organizations.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyChangesInProgressException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PolicyChangesInProgressException_:
    out: PolicyChangesInProgressException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class PolicyChangesInProgressException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#PolicyChangesInProgressException``."""

    code: str | None = "PolicyChangesInProgressException"

    def __init__(self, data: PolicyChangesInProgressException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicyChangesInProgressException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "PolicyChangesInProgressException":
        return cls(deserialize_aws_json_1_1(data))
