"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#AccessDeniedException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.access_denied_exception_reason


class AccessDeniedException_(TypedDict):
    message: "str"
    reason: "aws_sdk_partnercentral_account.types.access_denied_exception_reason.AccessDeniedExceptionReason"
    """<p>The specific reason for the access denial.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccessDeniedException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    import aws_sdk_partnercentral_account.types.access_denied_exception_reason

    out["Reason"] = (
        aws_sdk_partnercentral_account.types.access_denied_exception_reason.serialize_aws_json_1_0(
            value["reason"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("AccessDeniedException_.message required")
    if "Reason" in data:
        import aws_sdk_partnercentral_account.types.access_denied_exception_reason

        out["reason"] = (
            aws_sdk_partnercentral_account.types.access_denied_exception_reason.deserialize_aws_json_1_0(
                data["Reason"]
            )
        )
    else:
        raise DeserializationError("AccessDeniedException_.reason required")
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralaccount#AccessDeniedException``."""

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
    def from_aws_json_1_0(cls, data: dict) -> "AccessDeniedException":
        return cls(deserialize_aws_json_1_0(data))
