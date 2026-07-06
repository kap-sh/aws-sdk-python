"""Generated from Smithy shape ``com.amazonaws.organizations#InvalidResponsibilityTransferTransitionException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_organizations.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.exception_message


class InvalidResponsibilityTransferTransitionException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_organizations.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: InvalidResponsibilityTransferTransitionException_,
) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> InvalidResponsibilityTransferTransitionException_:
    out: InvalidResponsibilityTransferTransitionException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidResponsibilityTransferTransitionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#InvalidResponsibilityTransferTransitionException``."""

    code: str | None = "InvalidResponsibilityTransferTransitionException"

    def __init__(self, data: InvalidResponsibilityTransferTransitionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidResponsibilityTransferTransitionException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "InvalidResponsibilityTransferTransitionException":
        return cls(deserialize_aws_json_1_1(data))
