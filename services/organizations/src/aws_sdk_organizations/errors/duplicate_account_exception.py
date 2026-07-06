"""Generated from Smithy shape ``com.amazonaws.organizations#DuplicateAccountException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_organizations.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.exception_message


class DuplicateAccountException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_organizations.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DuplicateAccountException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DuplicateAccountException_:
    out: DuplicateAccountException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DuplicateAccountException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#DuplicateAccountException``."""

    code: str | None = "DuplicateAccountException"

    def __init__(self, data: DuplicateAccountException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicateAccountException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DuplicateAccountException":
        return cls(deserialize_aws_json_1_1(data))
