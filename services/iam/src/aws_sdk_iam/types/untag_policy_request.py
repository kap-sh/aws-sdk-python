"""Generated from Smithy shape ``com.amazonaws.iam#UntagPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.arn_type
    import aws_sdk_iam.types.tag_key_list_type


class UntagPolicyRequest(TypedDict):
    policy_arn: "aws_sdk_iam.types.arn_type.arnType"
    r"""<p>The ARN of the IAM customer managed policy from which you want to remove tags.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    tag_keys: "aws_sdk_iam.types.tag_key_list_type.tagKeyListType"
    """<p>A list of key names as a simple array of strings. The tags with matching keys are removed from the specified policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UntagPolicyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.PolicyArn", str(value["policy_arn"])))
    import aws_sdk_iam.types.tag_key_list_type

    aws_sdk_iam.types.tag_key_list_type.serialize_query(
        value["tag_keys"], pairs, f"{prefix}.TagKeys"
    )


def deserialize_query(el: Element) -> UntagPolicyRequest:
    out: UntagPolicyRequest = {}  # type: ignore[typeddict-item]
    child_policy_arn = el.find("PolicyArn")
    if child_policy_arn is not None:
        out["policy_arn"] = str(child_policy_arn.text or "")
    else:
        raise DeserializationError("UntagPolicyRequest.policy_arn required")
    child_tag_keys = el.find("TagKeys")
    if child_tag_keys is not None:
        import aws_sdk_iam.types.tag_key_list_type

        out["tag_keys"] = aws_sdk_iam.types.tag_key_list_type.deserialize_query(
            child_tag_keys
        )
    else:
        raise DeserializationError("UntagPolicyRequest.tag_keys required")
    return out
