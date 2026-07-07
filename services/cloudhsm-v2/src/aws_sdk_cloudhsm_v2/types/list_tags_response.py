"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#ListTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudhsm_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.next_token
    import aws_sdk_cloudhsm_v2.types.tag_list


class ListTagsResponse(TypedDict, closed=True):
    tag_list: "aws_sdk_cloudhsm_v2.types.tag_list.TagList"
    """<p>A list of tags.</p>"""
    next_token: NotRequired["aws_sdk_cloudhsm_v2.types.next_token.NextToken"]
    """<p>An opaque string that indicates that the response contains only a subset of tags. Use this value in a subsequent <code>ListTags</code> request to get more tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsResponse) -> dict:
    out: dict = {}
    import aws_sdk_cloudhsm_v2.types.tag_list

    out["TagList"] = aws_sdk_cloudhsm_v2.types.tag_list.serialize_aws_json_1_1(
        value["tag_list"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsResponse:
    out: ListTagsResponse = {}  # type: ignore[typeddict-item]
    if "TagList" in data:
        import aws_sdk_cloudhsm_v2.types.tag_list

        out["tag_list"] = aws_sdk_cloudhsm_v2.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    else:
        raise DeserializationError("ListTagsResponse.tag_list required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
