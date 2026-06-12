"""Generated from Smithy shape ``com.amazonaws.sns#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sns.types.amazon_resource_name
    import aws_sdk_sns.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_sns.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the topic from which to remove tags.</p>"""
    tag_keys: "aws_sdk_sns.types.tag_key_list.TagKeyList"
    """<p>The list of tag keys to remove from the specified topic.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UntagResourceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.ResourceArn", str(value["resource_arn"])))
    import aws_sdk_sns.types.tag_key_list

    aws_sdk_sns.types.tag_key_list.serialize_query(
        value["tag_keys"], pairs, f"{prefix}.TagKeys"
    )


def deserialize_query(el: Element) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    child_tag_keys = el.find("TagKeys")
    if child_tag_keys is not None:
        import aws_sdk_sns.types.tag_key_list

        out["tag_keys"] = aws_sdk_sns.types.tag_key_list.deserialize_query(
            child_tag_keys
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
