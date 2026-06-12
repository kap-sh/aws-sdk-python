"""Generated from Smithy shape ``com.amazonaws.ssooidc#InvalidScopeException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sso_oidc.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sso_oidc.types.error
    import aws_sdk_sso_oidc.types.error_description


class InvalidScopeException_(TypedDict):
    error: NotRequired["aws_sdk_sso_oidc.types.error.Error"]
    """<p>Single error code. For this exception the value will be <code>invalid_scope</code>.</p>"""
    error_description: NotRequired[
        "aws_sdk_sso_oidc.types.error_description.ErrorDescription"
    ]
    """<p>Human-readable text providing additional information, used to assist the client developer in understanding the error that occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidScopeException_) -> dict:
    out: dict = {}
    if "error" in value:
        out["error"] = value["error"]
    if "error_description" in value:
        out["error_description"] = value["error_description"]
    return out


def deserialize_json(data: dict) -> InvalidScopeException_:
    out: InvalidScopeException_ = {}  # type: ignore[typeddict-item]
    if "error" in data:
        out["error"] = data["error"]
    if "error_description" in data:
        out["error_description"] = data["error_description"]
    return out


class InvalidScopeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssooidc#InvalidScopeException``."""

    code: str | None = "InvalidScopeException"

    def __init__(self, data: InvalidScopeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidScopeException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidScopeException":
        return cls(deserialize_json(data))
