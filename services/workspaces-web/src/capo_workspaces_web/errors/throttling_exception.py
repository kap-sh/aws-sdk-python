"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workspaces_web.errors import ServiceError

if TYPE_CHECKING:
    import capo_workspaces_web.types.exception_message
    import capo_workspaces_web.types.quota_code
    import capo_workspaces_web.types.retry_after_seconds
    import capo_workspaces_web.types.service_code


class ThrottlingException_(TypedDict, closed=True):
    message: NotRequired["capo_workspaces_web.types.exception_message.ExceptionMessage"]
    service_code: NotRequired["capo_workspaces_web.types.service_code.ServiceCode"]
    """<p>The originating service.</p>"""
    quota_code: NotRequired["capo_workspaces_web.types.quota_code.QuotaCode"]
    """<p>The originating quota.</p>"""
    retry_after_seconds: (
        "capo_workspaces_web.types.retry_after_seconds.RetryAfterSeconds"
    )
    """<p>Advice to clients on when the call can be safely retried.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    if "quota_code" in value:
        out["quotaCode"] = value["quota_code"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    if "quotaCode" in data:
        out["quota_code"] = data["quotaCode"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspacesweb#ThrottlingException``."""

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
    def from_json(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_json(data))
