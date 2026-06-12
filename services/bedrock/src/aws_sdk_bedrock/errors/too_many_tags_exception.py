"""Generated from Smithy shape ``com.amazonaws.bedrock#TooManyTagsException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.non_blank_string
    import aws_sdk_bedrock.types.taggable_resources_arn


class TooManyTagsException_(TypedDict):
    message: NotRequired["aws_sdk_bedrock.types.non_blank_string.NonBlankString"]
    resource_name: NotRequired[
        "aws_sdk_bedrock.types.taggable_resources_arn.TaggableResourcesArn"
    ]
    """<p>The name of the resource with too many tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TooManyTagsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> TooManyTagsException_:
    out: TooManyTagsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    return out


class TooManyTagsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrock#TooManyTagsException``."""

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
