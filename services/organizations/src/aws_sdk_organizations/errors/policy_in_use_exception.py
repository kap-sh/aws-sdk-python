"""Generated from Smithy shape ``com.amazonaws.organizations#PolicyInUseException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_organizations.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.exception_message


class PolicyInUseException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_organizations.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyInUseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PolicyInUseException_:
    out: PolicyInUseException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class PolicyInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#PolicyInUseException``."""

    code: str | None = "PolicyInUseException"

    def __init__(self, data: PolicyInUseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicyInUseException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "PolicyInUseException":
        return cls(deserialize_aws_json_1_1(data))
