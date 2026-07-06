"""Generated from Smithy shape ``com.amazonaws.backup#ServiceUnavailableException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_backup.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_backup.types.string


class ServiceUnavailableException_(TypedDict, closed=True):
    code: NotRequired["aws_sdk_backup.types.string.string"]
    message: NotRequired["aws_sdk_backup.types.string.string"]
    type: NotRequired["aws_sdk_backup.types.string.string"]
    """<p></p>"""
    context: NotRequired["aws_sdk_backup.types.string.string"]
    """<p></p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceUnavailableException_) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    if "type" in value:
        out["Type"] = value["type"]
    if "context" in value:
        out["Context"] = value["context"]
    return out


def deserialize_json(data: dict) -> ServiceUnavailableException_:
    out: ServiceUnavailableException_ = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Context" in data:
        out["context"] = data["Context"]
    return out


class ServiceUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.backup#ServiceUnavailableException``."""

    code: str | None = "ServiceUnavailableException"

    def __init__(self, data: ServiceUnavailableException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceUnavailableException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ServiceUnavailableException":
        return cls(deserialize_json(data))
