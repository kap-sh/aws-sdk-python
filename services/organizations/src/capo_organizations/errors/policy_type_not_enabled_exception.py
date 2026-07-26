"""Generated from Smithy shape ``com.amazonaws.organizations#PolicyTypeNotEnabledException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_organizations.errors import ServiceError

if TYPE_CHECKING:
    import capo_organizations.types.exception_message


class PolicyTypeNotEnabledException_(TypedDict, closed=True):
    message: NotRequired["capo_organizations.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyTypeNotEnabledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PolicyTypeNotEnabledException_:
    out: PolicyTypeNotEnabledException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class PolicyTypeNotEnabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#PolicyTypeNotEnabledException``."""

    code: str | None = "PolicyTypeNotEnabledException"

    def __init__(self, data: PolicyTypeNotEnabledException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicyTypeNotEnabledException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "PolicyTypeNotEnabledException":
        return cls(deserialize_aws_json_1_1(data))
