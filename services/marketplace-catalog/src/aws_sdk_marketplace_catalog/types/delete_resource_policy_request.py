"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.resource_arn


class DeleteResourcePolicyRequest(TypedDict):
    resource_arn: "aws_sdk_marketplace_catalog.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the entity resource that is associated with the resource policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
