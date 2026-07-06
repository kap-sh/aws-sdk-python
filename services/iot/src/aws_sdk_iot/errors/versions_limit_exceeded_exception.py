"""Generated from Smithy shape ``com.amazonaws.iot#VersionsLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iot.types.error_message2


class VersionsLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_iot.types.error_message2.ErrorMessage2"]
    """<p>The message for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VersionsLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> VersionsLimitExceededException_:
    out: VersionsLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class VersionsLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iot#VersionsLimitExceededException``."""

    code: str | None = "VersionsLimitExceededException"

    def __init__(self, data: VersionsLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="VersionsLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "VersionsLimitExceededException":
        return cls(deserialize_json(data))
