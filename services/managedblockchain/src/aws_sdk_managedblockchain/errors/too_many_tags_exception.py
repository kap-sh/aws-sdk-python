"""Generated from Smithy shape ``com.amazonaws.managedblockchain#TooManyTagsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_managedblockchain.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.arn_string
    import aws_sdk_managedblockchain.types.exception_message


class TooManyTagsException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_managedblockchain.types.exception_message.ExceptionMessage"
    ]
    resource_name: NotRequired["aws_sdk_managedblockchain.types.arn_string.ArnString"]
    """<p></p>"""


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
    """Modeled error for Smithy shape ``com.amazonaws.managedblockchain#TooManyTagsException``."""

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
