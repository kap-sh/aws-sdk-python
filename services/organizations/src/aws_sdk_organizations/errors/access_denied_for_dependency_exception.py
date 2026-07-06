"""Generated from Smithy shape ``com.amazonaws.organizations#AccessDeniedForDependencyException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_organizations.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.access_denied_for_dependency_exception_reason
    import aws_sdk_organizations.types.exception_message


class AccessDeniedForDependencyException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_organizations.types.exception_message.ExceptionMessage"
    ]
    reason: NotRequired[
        "aws_sdk_organizations.types.access_denied_for_dependency_exception_reason.AccessDeniedForDependencyExceptionReason"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessDeniedForDependencyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import aws_sdk_organizations.types.access_denied_for_dependency_exception_reason

        out["Reason"] = (
            aws_sdk_organizations.types.access_denied_for_dependency_exception_reason.serialize_aws_json_1_1(
                value["reason"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessDeniedForDependencyException_:
    out: AccessDeniedForDependencyException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        import aws_sdk_organizations.types.access_denied_for_dependency_exception_reason

        out["reason"] = (
            aws_sdk_organizations.types.access_denied_for_dependency_exception_reason.deserialize_aws_json_1_1(
                data["Reason"]
            )
        )
    return out


class AccessDeniedForDependencyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#AccessDeniedForDependencyException``."""

    code: str | None = "AccessDeniedForDependencyException"

    def __init__(self, data: AccessDeniedForDependencyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedForDependencyException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AccessDeniedForDependencyException":
        return cls(deserialize_aws_json_1_1(data))
