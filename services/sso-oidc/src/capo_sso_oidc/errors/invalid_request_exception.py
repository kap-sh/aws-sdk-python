"""Generated from Smithy shape ``com.amazonaws.ssooidc#InvalidRequestException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sso_oidc.errors import ServiceError

if TYPE_CHECKING:
    import capo_sso_oidc.types.error
    import capo_sso_oidc.types.error_description
    import capo_sso_oidc.types.invalid_request_exception_reason


class InvalidRequestException_(TypedDict, closed=True):
    error: NotRequired["capo_sso_oidc.types.error.Error"]
    """<p>Single error code. For this exception the value will be <code>invalid_request</code>.</p>"""
    reason: NotRequired[
        "capo_sso_oidc.types.invalid_request_exception_reason.InvalidRequestExceptionReason"
    ]
    """<p>A string that uniquely identifies a reason for the error.</p>"""
    error_description: NotRequired[
        "capo_sso_oidc.types.error_description.ErrorDescription"
    ]
    """<p>Human-readable text providing additional information, used to assist the client developer in understanding the error that occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidRequestException_) -> dict:
    out: dict = {}
    if "error" in value:
        out["error"] = value["error"]
    if "reason" in value:
        import capo_sso_oidc.types.invalid_request_exception_reason

        out["reason"] = (
            capo_sso_oidc.types.invalid_request_exception_reason.serialize_json(
                value["reason"]
            )
        )
    if "error_description" in value:
        out["error_description"] = value["error_description"]
    return out


def deserialize_json(data: dict) -> InvalidRequestException_:
    out: InvalidRequestException_ = {}  # type: ignore[typeddict-item]
    if "error" in data:
        out["error"] = data["error"]
    if "reason" in data:
        import capo_sso_oidc.types.invalid_request_exception_reason

        out["reason"] = (
            capo_sso_oidc.types.invalid_request_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    if "error_description" in data:
        out["error_description"] = data["error_description"]
    return out


class InvalidRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssooidc#InvalidRequestException``."""

    code: str | None = "InvalidRequestException"

    def __init__(self, data: InvalidRequestException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRequestException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "InvalidRequestException":
        return cls(deserialize_json(data), message)
