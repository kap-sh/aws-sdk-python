"""Generated from Smithy shape ``com.amazonaws.ram#PromoteResourceShareCreatedFromPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ram.types.string


class PromoteResourceShareCreatedFromPolicyRequest(TypedDict):
    resource_share_arn: "aws_sdk_ram.types.string.String"
    r"""<p>Specifies the <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the resource share to promote.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromoteResourceShareCreatedFromPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PromoteResourceShareCreatedFromPolicyRequest:
    out: PromoteResourceShareCreatedFromPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
