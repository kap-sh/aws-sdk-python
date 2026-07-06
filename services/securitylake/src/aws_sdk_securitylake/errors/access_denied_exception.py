"""Generated from Smithy shape ``com.amazonaws.securitylake#AccessDeniedException``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_securitylake.errors import ServiceError


class AccessDeniedException_(TypedDict, closed=True):
    message: NotRequired["str"]
    error_code: NotRequired["str"]
    """<p>A coded string to provide more information about the access denied exception. You can use the error code to check the exception type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.securitylake#AccessDeniedException``."""

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
    def from_json(cls, data: dict) -> "AccessDeniedException":
        return cls(deserialize_json(data))
