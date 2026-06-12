"""Generated from Smithy shape ``com.amazonaws.organizations#DuplicatePolicyException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_organizations.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.exception_message


class DuplicatePolicyException_(TypedDict):
    message: NotRequired[
        "aws_sdk_organizations.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DuplicatePolicyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DuplicatePolicyException_:
    out: DuplicatePolicyException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DuplicatePolicyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#DuplicatePolicyException``."""

    code: str | None = "DuplicatePolicyException"

    def __init__(self, data: DuplicatePolicyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicatePolicyException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DuplicatePolicyException":
        return cls(deserialize_aws_json_1_1(data))
