"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.arn_string


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "aws_sdk_managedblockchain.types.arn_string.ArnString"
    r"""<p>The Amazon Resource Name (ARN) of the resource. For more information about ARNs and their format, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
