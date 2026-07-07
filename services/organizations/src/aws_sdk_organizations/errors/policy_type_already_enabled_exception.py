"""Generated from Smithy shape ``com.amazonaws.organizations#PolicyTypeAlreadyEnabledException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_organizations.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.exception_message


class PolicyTypeAlreadyEnabledException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_organizations.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyTypeAlreadyEnabledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PolicyTypeAlreadyEnabledException_:
    out: PolicyTypeAlreadyEnabledException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class PolicyTypeAlreadyEnabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#PolicyTypeAlreadyEnabledException``."""

    code: str | None = "PolicyTypeAlreadyEnabledException"

    def __init__(self, data: PolicyTypeAlreadyEnabledException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicyTypeAlreadyEnabledException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "PolicyTypeAlreadyEnabledException":
        return cls(deserialize_aws_json_1_1(data))
