"""Generated from Smithy shape ``com.amazonaws.ssooidc#InvalidRequestRegionException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sso_oidc.errors import ServiceError

if TYPE_CHECKING:
    import capo_sso_oidc.types.error
    import capo_sso_oidc.types.error_description
    import capo_sso_oidc.types.location
    import capo_sso_oidc.types.region


class InvalidRequestRegionException_(TypedDict, closed=True):
    error: NotRequired["capo_sso_oidc.types.error.Error"]
    """<p>Single error code. For this exception the value will be <code>invalid_request</code>.</p>"""
    error_description: NotRequired[
        "capo_sso_oidc.types.error_description.ErrorDescription"
    ]
    """<p>Human-readable text providing additional information, used to assist the client developer in understanding the error that occurred.</p>"""
    endpoint: NotRequired["capo_sso_oidc.types.location.Location"]
    """<p>Indicates the IAM Identity Center endpoint which the requester may call with this token.</p>"""
    region: NotRequired["capo_sso_oidc.types.region.Region"]
    """<p>Indicates the region which the requester may call with this token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidRequestRegionException_) -> dict:
    out: dict = {}
    if "error" in value:
        out["error"] = value["error"]
    if "error_description" in value:
        out["error_description"] = value["error_description"]
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    if "region" in value:
        out["region"] = value["region"]
    return out


def deserialize_json(data: dict) -> InvalidRequestRegionException_:
    out: InvalidRequestRegionException_ = {}  # type: ignore[typeddict-item]
    if "error" in data:
        out["error"] = data["error"]
    if "error_description" in data:
        out["error_description"] = data["error_description"]
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    if "region" in data:
        out["region"] = data["region"]
    return out


class InvalidRequestRegionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssooidc#InvalidRequestRegionException``."""

    code: str | None = "InvalidRequestRegionException"

    def __init__(
        self, data: InvalidRequestRegionException_, message: str | None = None
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRequestRegionException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "InvalidRequestRegionException":
        return cls(deserialize_json(data), message)
