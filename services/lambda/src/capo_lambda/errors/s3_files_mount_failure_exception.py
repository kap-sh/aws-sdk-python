"""Generated from Smithy shape ``com.amazonaws.lambda#S3FilesMountFailureException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import ServiceError

if TYPE_CHECKING:
    import capo_lambda.types.string


class S3FilesMountFailureException_(TypedDict, closed=True):
    type: NotRequired["capo_lambda.types.string.String"]
    """<p>The exception type.</p>"""
    message: NotRequired["capo_lambda.types.string.String"]
    """<p>The exception message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3FilesMountFailureException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> S3FilesMountFailureException_:
    out: S3FilesMountFailureException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class S3FilesMountFailureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#S3FilesMountFailureException``."""

    code: str | None = "S3FilesMountFailureException"

    def __init__(self, data: S3FilesMountFailureException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="S3FilesMountFailureException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "S3FilesMountFailureException":
        return cls(deserialize_json(data))
