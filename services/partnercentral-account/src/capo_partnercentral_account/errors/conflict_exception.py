"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_account.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.conflict_exception_reason


class ConflictException_(TypedDict, closed=True):
    message: "str"
    reason: "capo_partnercentral_account.types.conflict_exception_reason.ConflictExceptionReason"
    """<p>The specific reason for the conflict.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConflictException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    import capo_partnercentral_account.types.conflict_exception_reason

    out["Reason"] = (
        capo_partnercentral_account.types.conflict_exception_reason.serialize_aws_json_1_0(
            value["reason"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    if "Reason" in data:
        import capo_partnercentral_account.types.conflict_exception_reason

        out["reason"] = (
            capo_partnercentral_account.types.conflict_exception_reason.deserialize_aws_json_1_0(
                data["Reason"]
            )
        )
    else:
        raise DeserializationError("ConflictException_.reason required")
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralaccount#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ConflictException":
        return cls(deserialize_aws_json_1_0(data))
