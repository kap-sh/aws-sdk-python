"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TooManyTagsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_meetings.errors import ServiceError

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.amazon_resource_name
    import capo_chime_sdk_meetings.types.string


class TooManyTagsException_(TypedDict, closed=True):
    code: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    message: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    request_id: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    """<p>The ID of the request that contains too many tags.</p>"""
    resource_name: NotRequired[
        "capo_chime_sdk_meetings.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The name of the resource that received too many tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TooManyTagsException_) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> TooManyTagsException_:
    out: TooManyTagsException_ = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    return out


class TooManyTagsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chimesdkmeetings#TooManyTagsException``."""

    code: str | None = "TooManyTagsException"

    def __init__(self, data: TooManyTagsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyTagsException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TooManyTagsException":
        return cls(deserialize_json(data))
