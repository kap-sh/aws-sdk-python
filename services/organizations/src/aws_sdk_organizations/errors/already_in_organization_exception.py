"""Generated from Smithy shape ``com.amazonaws.organizations#AlreadyInOrganizationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_organizations.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.exception_message


class AlreadyInOrganizationException_(TypedDict):
    message: NotRequired[
        "aws_sdk_organizations.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlreadyInOrganizationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AlreadyInOrganizationException_:
    out: AlreadyInOrganizationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AlreadyInOrganizationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#AlreadyInOrganizationException``."""

    code: str | None = "AlreadyInOrganizationException"

    def __init__(self, data: AlreadyInOrganizationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AlreadyInOrganizationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AlreadyInOrganizationException":
        return cls(deserialize_aws_json_1_1(data))
