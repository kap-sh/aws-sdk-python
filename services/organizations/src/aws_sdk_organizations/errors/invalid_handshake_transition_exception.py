"""Generated from Smithy shape ``com.amazonaws.organizations#InvalidHandshakeTransitionException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_organizations.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.exception_message


class InvalidHandshakeTransitionException_(TypedDict):
    message: NotRequired[
        "aws_sdk_organizations.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidHandshakeTransitionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidHandshakeTransitionException_:
    out: InvalidHandshakeTransitionException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidHandshakeTransitionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#InvalidHandshakeTransitionException``."""

    code: str | None = "InvalidHandshakeTransitionException"

    def __init__(self, data: InvalidHandshakeTransitionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidHandshakeTransitionException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidHandshakeTransitionException":
        return cls(deserialize_aws_json_1_1(data))
