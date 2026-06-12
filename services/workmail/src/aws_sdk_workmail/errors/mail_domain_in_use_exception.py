"""Generated from Smithy shape ``com.amazonaws.workmail#MailDomainInUseException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workmail.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.string


class MailDomainInUseException_(TypedDict):
    message: NotRequired["aws_sdk_workmail.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MailDomainInUseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MailDomainInUseException_:
    out: MailDomainInUseException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class MailDomainInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workmail#MailDomainInUseException``."""

    code: str | None = "MailDomainInUseException"

    def __init__(self, data: MailDomainInUseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MailDomainInUseException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "MailDomainInUseException":
        return cls(deserialize_aws_json_1_1(data))
