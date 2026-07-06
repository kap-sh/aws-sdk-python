"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#GetResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.resource_arn


class GetResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_marketplace_catalog.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the entity resource that is associated with the resource policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourcePolicyRequest:
    out: GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
