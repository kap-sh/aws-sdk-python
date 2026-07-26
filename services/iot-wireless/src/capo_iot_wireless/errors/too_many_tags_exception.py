"""Generated from Smithy shape ``com.amazonaws.iotwireless#TooManyTagsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot_wireless.errors import ServiceError

if TYPE_CHECKING:
    import capo_iot_wireless.types.amazon_resource_name
    import capo_iot_wireless.types.message


class TooManyTagsException_(TypedDict, closed=True):
    message: NotRequired["capo_iot_wireless.types.message.Message"]
    resource_name: NotRequired[
        "capo_iot_wireless.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>Name of the resource that exceeds maximum number of tags allowed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TooManyTagsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> TooManyTagsException_:
    out: TooManyTagsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    return out


class TooManyTagsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotwireless#TooManyTagsException``."""

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
