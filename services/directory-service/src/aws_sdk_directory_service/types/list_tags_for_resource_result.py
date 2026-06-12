"""Generated from Smithy shape ``com.amazonaws.directoryservice#ListTagsForResourceResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.next_token
    import aws_sdk_directory_service.types.tags


class ListTagsForResourceResult(TypedDict):
    tags: NotRequired["aws_sdk_directory_service.types.tags.Tags"]
    """<p>List of tags returned by the ListTagsForResource operation.</p>"""
    next_token: NotRequired["aws_sdk_directory_service.types.next_token.NextToken"]
    """<p>Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResult) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_directory_service.types.tags

        out["Tags"] = aws_sdk_directory_service.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResult:
    out: ListTagsForResourceResult = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_directory_service.types.tags

        out["tags"] = aws_sdk_directory_service.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
