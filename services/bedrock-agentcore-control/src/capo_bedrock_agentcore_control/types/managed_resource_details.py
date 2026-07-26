"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ManagedResourceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.domain_name
    import capo_bedrock_agentcore_control.types.resource_association_arn
    import capo_bedrock_agentcore_control.types.resource_gateway_arn


class ManagedResourceDetails(TypedDict, closed=True):
    domain: NotRequired["capo_bedrock_agentcore_control.types.domain_name.DomainName"]
    """<p>The domain associated with this managed resource.</p>"""
    resource_gateway_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.resource_gateway_arn.ResourceGatewayArn"
    ]
    """<p>The ARN of the VPC Lattice resource gateway created in your account.</p>"""
    resource_association_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.resource_association_arn.ResourceAssociationArn"
    ]
    """<p>The ARN of the service network resource association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedResourceDetails) -> dict:
    out: dict = {}
    if "domain" in value:
        out["domain"] = value["domain"]
    if "resource_gateway_arn" in value:
        out["resourceGatewayArn"] = value["resource_gateway_arn"]
    if "resource_association_arn" in value:
        out["resourceAssociationArn"] = value["resource_association_arn"]
    return out


def deserialize_json(data: dict) -> ManagedResourceDetails:
    out: ManagedResourceDetails = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    if "resourceGatewayArn" in data:
        out["resource_gateway_arn"] = data["resourceGatewayArn"]
    if "resourceAssociationArn" in data:
        out["resource_association_arn"] = data["resourceAssociationArn"]
    return out
