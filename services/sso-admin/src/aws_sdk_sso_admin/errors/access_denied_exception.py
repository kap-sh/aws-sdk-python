"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AccessDeniedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sso_admin.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.access_denied_exception_message
    import aws_sdk_sso_admin.types.access_denied_exception_reason


class AccessDeniedException_(TypedDict):
    message: NotRequired[
        "aws_sdk_sso_admin.types.access_denied_exception_message.AccessDeniedExceptionMessage"
    ]
    reason: NotRequired[
        "aws_sdk_sso_admin.types.access_denied_exception_reason.AccessDeniedExceptionReason"
    ]
    """<p>The reason for the access denied exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import aws_sdk_sso_admin.types.access_denied_exception_reason

        out["Reason"] = (
            aws_sdk_sso_admin.types.access_denied_exception_reason.serialize_aws_json_1_1(
                value["reason"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        import aws_sdk_sso_admin.types.access_denied_exception_reason

        out["reason"] = (
            aws_sdk_sso_admin.types.access_denied_exception_reason.deserialize_aws_json_1_1(
                data["Reason"]
            )
        )
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssoadmin#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(self, data: AccessDeniedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AccessDeniedException":
        return cls(deserialize_aws_json_1_1(data))
