"""Generated from Smithy shape ``com.amazonaws.organizations#HandshakeConstraintViolationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_organizations.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.exception_message
    import aws_sdk_organizations.types.handshake_constraint_violation_exception_reason


class HandshakeConstraintViolationException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_organizations.types.exception_message.ExceptionMessage"
    ]
    reason: NotRequired[
        "aws_sdk_organizations.types.handshake_constraint_violation_exception_reason.HandshakeConstraintViolationExceptionReason"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HandshakeConstraintViolationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import aws_sdk_organizations.types.handshake_constraint_violation_exception_reason

        out["Reason"] = (
            aws_sdk_organizations.types.handshake_constraint_violation_exception_reason.serialize_aws_json_1_1(
                value["reason"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HandshakeConstraintViolationException_:
    out: HandshakeConstraintViolationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        import aws_sdk_organizations.types.handshake_constraint_violation_exception_reason

        out["reason"] = (
            aws_sdk_organizations.types.handshake_constraint_violation_exception_reason.deserialize_aws_json_1_1(
                data["Reason"]
            )
        )
    return out


class HandshakeConstraintViolationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#HandshakeConstraintViolationException``."""

    code: str | None = "HandshakeConstraintViolationException"

    def __init__(self, data: HandshakeConstraintViolationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="HandshakeConstraintViolationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "HandshakeConstraintViolationException":
        return cls(deserialize_aws_json_1_1(data))
