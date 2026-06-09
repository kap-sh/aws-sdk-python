"""Generated from Smithy shape ``com.amazonaws.iam#TagPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.arn_type
    import aws_sdk_iam.types.tag_list_type


class TagPolicyRequest(TypedDict):
    policy_arn: "aws_sdk_iam.types.arn_type.arnType"
    """<p>The ARN of the IAM customer managed policy to which you want to add tags.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    tags: "aws_sdk_iam.types.tag_list_type.tagListType"
    """<p>The list of tags that you want to attach to the IAM customer managed policy. Each tag consists of a key name and an associated value.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TagPolicyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.PolicyArn", str(value["policy_arn"])))
    import aws_sdk_iam.types.tag_list_type

    aws_sdk_iam.types.tag_list_type.serialize_query(
        value["tags"], pairs, f"{prefix}.Tags"
    )


def deserialize_query(el: Element) -> TagPolicyRequest:
    out: TagPolicyRequest = {}  # type: ignore[typeddict-item]
    child_policy_arn = el.find("PolicyArn")
    if child_policy_arn is not None:
        out["policy_arn"] = str(child_policy_arn.text or "")
    else:
        raise DeserializationError("TagPolicyRequest.policy_arn required")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_iam.types.tag_list_type

        out["tags"] = aws_sdk_iam.types.tag_list_type.deserialize_query(child_tags)
    else:
        raise DeserializationError("TagPolicyRequest.tags required")
    return out
