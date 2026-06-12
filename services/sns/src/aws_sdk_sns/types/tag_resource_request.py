"""Generated from Smithy shape ``com.amazonaws.sns#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sns.types.amazon_resource_name
    import aws_sdk_sns.types.tag_list


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_sns.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the topic to which to add tags.</p>"""
    tags: "aws_sdk_sns.types.tag_list.TagList"
    """<p>The tags to be added to the specified topic. A tag consists of a required key and an optional value.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TagResourceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.ResourceArn", str(value["resource_arn"])))
    import aws_sdk_sns.types.tag_list

    aws_sdk_sns.types.tag_list.serialize_query(value["tags"], pairs, f"{prefix}.Tags")


def deserialize_query(el: Element) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_sns.types.tag_list

        out["tags"] = aws_sdk_sns.types.tag_list.deserialize_query(child_tags)
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
