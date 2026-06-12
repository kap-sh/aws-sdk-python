"""Generated from Smithy shape ``com.amazonaws.organizations#ConstraintViolationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_organizations.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.constraint_violation_exception_reason
    import aws_sdk_organizations.types.exception_message


class ConstraintViolationException_(TypedDict):
    message: NotRequired[
        "aws_sdk_organizations.types.exception_message.ExceptionMessage"
    ]
    reason: NotRequired[
        "aws_sdk_organizations.types.constraint_violation_exception_reason.ConstraintViolationExceptionReason"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConstraintViolationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import aws_sdk_organizations.types.constraint_violation_exception_reason

        out["Reason"] = (
            aws_sdk_organizations.types.constraint_violation_exception_reason.serialize_aws_json_1_1(
                value["reason"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConstraintViolationException_:
    out: ConstraintViolationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        import aws_sdk_organizations.types.constraint_violation_exception_reason

        out["reason"] = (
            aws_sdk_organizations.types.constraint_violation_exception_reason.deserialize_aws_json_1_1(
                data["Reason"]
            )
        )
    return out


class ConstraintViolationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#ConstraintViolationException``."""

    code: str | None = "ConstraintViolationException"

    def __init__(self, data: ConstraintViolationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConstraintViolationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ConstraintViolationException":
        return cls(deserialize_aws_json_1_1(data))
