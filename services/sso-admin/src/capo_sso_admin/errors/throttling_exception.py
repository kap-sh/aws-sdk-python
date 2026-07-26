"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sso_admin.errors import ServiceError

if TYPE_CHECKING:
    import capo_sso_admin.types.throttling_exception_message
    import capo_sso_admin.types.throttling_exception_reason


class ThrottlingException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_sso_admin.types.throttling_exception_message.ThrottlingExceptionMessage"
    ]
    reason: NotRequired[
        "capo_sso_admin.types.throttling_exception_reason.ThrottlingExceptionReason"
    ]
    """<p>The reason for the throttling exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThrottlingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import capo_sso_admin.types.throttling_exception_reason

        out["Reason"] = (
            capo_sso_admin.types.throttling_exception_reason.serialize_aws_json_1_1(
                value["reason"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        import capo_sso_admin.types.throttling_exception_reason

        out["reason"] = (
            capo_sso_admin.types.throttling_exception_reason.deserialize_aws_json_1_1(
                data["Reason"]
            )
        )
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssoadmin#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_aws_json_1_1(data))
