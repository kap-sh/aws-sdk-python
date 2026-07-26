"""Generated from Smithy shape ``com.amazonaws.ssooidc#UnsupportedGrantTypeException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sso_oidc.errors import ServiceError

if TYPE_CHECKING:
    import capo_sso_oidc.types.error
    import capo_sso_oidc.types.error_description


class UnsupportedGrantTypeException_(TypedDict, closed=True):
    error: NotRequired["capo_sso_oidc.types.error.Error"]
    """<p>Single error code. For this exception the value will be <code>unsupported_grant_type</code>.</p>"""
    error_description: NotRequired[
        "capo_sso_oidc.types.error_description.ErrorDescription"
    ]
    """<p>Human-readable text providing additional information, used to assist the client developer in understanding the error that occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnsupportedGrantTypeException_) -> dict:
    out: dict = {}
    if "error" in value:
        out["error"] = value["error"]
    if "error_description" in value:
        out["error_description"] = value["error_description"]
    return out


def deserialize_json(data: dict) -> UnsupportedGrantTypeException_:
    out: UnsupportedGrantTypeException_ = {}  # type: ignore[typeddict-item]
    if "error" in data:
        out["error"] = data["error"]
    if "error_description" in data:
        out["error_description"] = data["error_description"]
    return out


class UnsupportedGrantTypeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssooidc#UnsupportedGrantTypeException``."""

    code: str | None = "UnsupportedGrantTypeException"

    def __init__(self, data: UnsupportedGrantTypeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedGrantTypeException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnsupportedGrantTypeException":
        return cls(deserialize_json(data))
