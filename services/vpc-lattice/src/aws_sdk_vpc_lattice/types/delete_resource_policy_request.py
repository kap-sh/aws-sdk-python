"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.resource_arn


class DeleteResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_vpc_lattice.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
