"""Generated from Smithy shape ``com.amazonaws.backup#AlreadyExistsException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_backup.errors import ServiceError
if TYPE_CHECKING:
    import aws_sdk_backup.types.string

class AlreadyExistsException_(TypedDict):
    code: NotRequired["aws_sdk_backup.types.string.string"]
    message: NotRequired["aws_sdk_backup.types.string.string"]
    creator_request_id: NotRequired["aws_sdk_backup.types.string.string"]
    """<p></p>"""
    arn: NotRequired["aws_sdk_backup.types.string.string"]
    """<p></p>"""
    type: NotRequired["aws_sdk_backup.types.string.string"]
    """<p></p>"""
    context: NotRequired["aws_sdk_backup.types.string.string"]
    """<p></p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AlreadyExistsException_) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "type" in value:
        out["Type"] = value["type"]
    if "context" in value:
        out["Context"] = value["context"]
    return out


def deserialize_json(data: dict) -> AlreadyExistsException_:
    out: AlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Message" in data:
        out["message"] = data["Message"]
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Context" in data:
        out["context"] = data["Context"]
    return out


class AlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.backup#AlreadyExistsException``."""
    code: str | None = 'AlreadyExistsException'

    def __init__(self, data: AlreadyExistsException_):
        super().__init__('client', is_throttling_error=False, is_retryable=False, code='AlreadyExistsException')
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "AlreadyExistsException":
        return cls(deserialize_json(data))