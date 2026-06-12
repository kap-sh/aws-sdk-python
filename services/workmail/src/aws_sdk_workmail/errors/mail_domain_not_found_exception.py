"""Generated from Smithy shape ``com.amazonaws.workmail#MailDomainNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workmail.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.string


class MailDomainNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_workmail.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MailDomainNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MailDomainNotFoundException_:
    out: MailDomainNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class MailDomainNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workmail#MailDomainNotFoundException``."""

    code: str | None = "MailDomainNotFoundException"

    def __init__(self, data: MailDomainNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MailDomainNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "MailDomainNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
