"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#InternalServerException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces_thin_client.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workspaces_thin_client.types.exception_message
    import aws_sdk_workspaces_thin_client.types.retry_after_seconds


class InternalServerException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_workspaces_thin_client.types.exception_message.ExceptionMessage"
    ]
    retry_after_seconds: NotRequired[
        "aws_sdk_workspaces_thin_client.types.retry_after_seconds.RetryAfterSeconds"
    ]
    """<p>The number of seconds to wait before retrying the next request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspacesthinclient#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(self, data: InternalServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalServerException":
        return cls(deserialize_json(data))
