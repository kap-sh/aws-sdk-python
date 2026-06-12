"""Generated from Smithy shape ``com.amazonaws.ivs#StreamUnavailable``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.error_message
    import aws_sdk_ivs.types.string


class StreamUnavailable_(TypedDict):
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
    """<p>The stream is temporarily unavailable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamUnavailable_) -> dict:
    out: dict = {}
    if "exception_message" in value:
        out["exceptionMessage"] = value["exception_message"]
    return out


def deserialize_json(data: dict) -> StreamUnavailable_:
    out: StreamUnavailable_ = {}  # type: ignore[typeddict-item]
    if "exceptionMessage" in data:
        out["exception_message"] = data["exceptionMessage"]
    return out


class StreamUnavailable(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ivs#StreamUnavailable``."""

    code: str | None = "StreamUnavailable"

    def __init__(self, data: StreamUnavailable_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="StreamUnavailable",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "StreamUnavailable":
        return cls(deserialize_json(data))
