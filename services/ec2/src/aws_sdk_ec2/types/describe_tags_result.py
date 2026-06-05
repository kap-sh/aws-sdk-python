"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTagsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_description_list


class DescribeTagsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_description_list.TagDescriptionList"]
    """<p>The tags.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTagsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_description_list

        aws_sdk_ec2.types.tag_description_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeTagsResult:
    out: DescribeTagsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_description_list

        out["tags"] = aws_sdk_ec2.types.tag_description_list.deserialize_ec2_query(
            el, "TagSet"
        )
    return out
