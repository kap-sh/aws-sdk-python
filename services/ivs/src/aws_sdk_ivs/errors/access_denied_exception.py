"""Generated from Smithy shape ``com.amazonaws.ivs#AccessDeniedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ivs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.error_message
    import aws_sdk_ivs.types.string


class AccessDeniedException_(TypedDict, closed=True):
    access_control_allow_origin: NotRequired["aws_sdk_ivs.types.string.String"]
    """<p/>"""
    access_control_expose_headers: NotRequired["aws_sdk_ivs.types.string.String"]
    """<p/>"""
    cache_control: NotRequired["aws_sdk_ivs.types.string.String"]
    """<p/>"""
    content_security_policy: NotRequired["aws_sdk_ivs.types.string.String"]
    """<p/>"""
    strict_transport_security: NotRequired["aws_sdk_ivs.types.string.String"]
    """<p/>"""
    x_content_type_options: NotRequired["aws_sdk_ivs.types.string.String"]
    """<p/>"""
    x_frame_options: NotRequired["aws_sdk_ivs.types.string.String"]
    """<p/>"""
    x_amzn_error_type: NotRequired["aws_sdk_ivs.types.string.String"]
    """<p/>"""
    exception_message: NotRequired["aws_sdk_ivs.types.error_message.errorMessage"]
    """<p>User does not have sufficient access to perform this action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "exception_message" in value:
        out["exceptionMessage"] = value["exception_message"]
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "exceptionMessage" in data:
        out["exception_message"] = data["exceptionMessage"]
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ivs#AccessDeniedException``."""

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
