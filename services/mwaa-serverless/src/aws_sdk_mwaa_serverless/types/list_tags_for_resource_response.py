"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.tags


class ListTagsForResourceResponse(TypedDict):
    tags: NotRequired["aws_sdk_mwaa_serverless.types.tags.Tags"]
    """<p>A map of tags that are associated with the resource, where each tag consists of a key-value pair.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_mwaa_serverless.types.tags

        out["Tags"] = aws_sdk_mwaa_serverless.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_mwaa_serverless.types.tags

        out["tags"] = aws_sdk_mwaa_serverless.types.tags.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
