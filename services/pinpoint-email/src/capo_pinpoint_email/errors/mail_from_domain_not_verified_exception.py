"""Generated from Smithy shape ``com.amazonaws.pinpointemail#MailFromDomainNotVerifiedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_email.errors import ServiceError

if TYPE_CHECKING:
    import capo_pinpoint_email.types.error_message


class MailFromDomainNotVerifiedException_(TypedDict, closed=True):
    message: NotRequired["capo_pinpoint_email.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: MailFromDomainNotVerifiedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MailFromDomainNotVerifiedException_:
    out: MailFromDomainNotVerifiedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class MailFromDomainNotVerifiedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pinpointemail#MailFromDomainNotVerifiedException``."""

    code: str | None = "MailFromDomainNotVerifiedException"

    def __init__(self, data: MailFromDomainNotVerifiedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MailFromDomainNotVerifiedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "MailFromDomainNotVerifiedException":
        return cls(deserialize_json(data))
