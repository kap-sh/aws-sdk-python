"""Generated from Smithy shape ``com.amazonaws.organizations#FinalizingOrganizationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_organizations.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.exception_message


class FinalizingOrganizationException_(TypedDict):
    message: NotRequired[
        "aws_sdk_organizations.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FinalizingOrganizationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FinalizingOrganizationException_:
    out: FinalizingOrganizationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class FinalizingOrganizationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#FinalizingOrganizationException``."""

    code: str | None = "FinalizingOrganizationException"

    def __init__(self, data: FinalizingOrganizationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FinalizingOrganizationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "FinalizingOrganizationException":
        return cls(deserialize_aws_json_1_1(data))
