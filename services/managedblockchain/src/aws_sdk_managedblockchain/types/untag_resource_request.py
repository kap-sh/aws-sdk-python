"""Generated from Smithy shape ``com.amazonaws.managedblockchain#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.arn_string
    import aws_sdk_managedblockchain.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_managedblockchain.types.arn_string.ArnString"
    r"""<p>The Amazon Resource Name (ARN) of the resource. For more information about ARNs and their format, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    tag_keys: "aws_sdk_managedblockchain.types.tag_key_list.TagKeyList"
    """<p>The tag keys.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
