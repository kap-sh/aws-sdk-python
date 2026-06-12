"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteTagsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of__string
    import aws_sdk_medialive.types.__string


class DeleteTagsRequest(TypedDict):
    resource_arn: "aws_sdk_medialive.types.__string.__string"
    tag_keys: NotRequired["aws_sdk_medialive.types.__list_of__string.__listOf__string"]
    """An array of tag keys to delete"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTagsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTagsRequest:
    out: DeleteTagsRequest = {}  # type: ignore[typeddict-item]
    return out
