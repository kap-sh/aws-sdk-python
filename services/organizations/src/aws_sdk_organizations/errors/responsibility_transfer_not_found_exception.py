"""Generated from Smithy shape ``com.amazonaws.organizations#ResponsibilityTransferNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_organizations.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.exception_message


class ResponsibilityTransferNotFoundException_(TypedDict):
    message: NotRequired[
        "aws_sdk_organizations.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponsibilityTransferNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResponsibilityTransferNotFoundException_:
    out: ResponsibilityTransferNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResponsibilityTransferNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#ResponsibilityTransferNotFoundException``."""

    code: str | None = "ResponsibilityTransferNotFoundException"

    def __init__(self, data: ResponsibilityTransferNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResponsibilityTransferNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResponsibilityTransferNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
