"""Generated from Smithy shape ``com.amazonaws.chime#ResourceLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_chime.types.error_code
    import aws_sdk_chime.types.string


class ResourceLimitExceededException_(TypedDict, closed=True):
    code: NotRequired["aws_sdk_chime.types.error_code.ErrorCode"]
    message: NotRequired["aws_sdk_chime.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceLimitExceededException_) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_chime.types.error_code

        out["Code"] = aws_sdk_chime.types.error_code.serialize_json(value["code"])
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceLimitExceededException_:
    out: ResourceLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import aws_sdk_chime.types.error_code

        out["code"] = aws_sdk_chime.types.error_code.deserialize_json(data["Code"])
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chime#ResourceLimitExceededException``."""

    code: str | None = "ResourceLimitExceededException"

    def __init__(self, data: ResourceLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceLimitExceededException":
        return cls(deserialize_json(data))
