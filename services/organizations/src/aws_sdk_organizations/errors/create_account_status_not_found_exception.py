"""Generated from Smithy shape ``com.amazonaws.organizations#CreateAccountStatusNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_organizations.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.exception_message


class CreateAccountStatusNotFoundException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_organizations.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAccountStatusNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAccountStatusNotFoundException_:
    out: CreateAccountStatusNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class CreateAccountStatusNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#CreateAccountStatusNotFoundException``."""

    code: str | None = "CreateAccountStatusNotFoundException"

    def __init__(self, data: CreateAccountStatusNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CreateAccountStatusNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "CreateAccountStatusNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
