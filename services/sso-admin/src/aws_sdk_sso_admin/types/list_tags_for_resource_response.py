"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.tag_list
    import aws_sdk_sso_admin.types.token


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_sso_admin.types.tag_list.TagList"]
    """<p>A set of key-value pairs that are used to manage the resource.</p>"""
    next_token: NotRequired["aws_sdk_sso_admin.types.token.Token"]
    """<p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_sso_admin.types.tag_list

        out["Tags"] = aws_sdk_sso_admin.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_sso_admin.types.tag_list

        out["tags"] = aws_sdk_sso_admin.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
