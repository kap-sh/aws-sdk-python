"""Generated from Smithy shape ``com.amazonaws.networkmanager#NetworkResourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.boolean
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.resource_arn


class NetworkResourceSummary(TypedDict, closed=True):
    registered_gateway_arn: NotRequired[
        "capo_networkmanager.types.resource_arn.ResourceArn"
    ]
    """<p>The ARN of the gateway.</p>"""
    resource_arn: NotRequired["capo_networkmanager.types.resource_arn.ResourceArn"]
    """<p>The ARN of the resource.</p>"""
    resource_type: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The resource type.</p>"""
    definition: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>Information about the resource, in JSON format. Network Manager gets this information by describing the resource using its Describe API call.</p>"""
    name_tag: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The value for the Name tag.</p>"""
    is_middlebox: "capo_networkmanager.types.boolean.Boolean"
    """<p>Indicates whether this is a middlebox appliance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkResourceSummary) -> dict:
    out: dict = {}
    if "registered_gateway_arn" in value:
        out["RegisteredGatewayArn"] = value["registered_gateway_arn"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "definition" in value:
        out["Definition"] = value["definition"]
    if "name_tag" in value:
        out["NameTag"] = value["name_tag"]
    out["IsMiddlebox"] = value.get("is_middlebox", False)
    return out


def deserialize_json(data: dict) -> NetworkResourceSummary:
    out: NetworkResourceSummary = {}  # type: ignore[typeddict-item]
    if "RegisteredGatewayArn" in data:
        out["registered_gateway_arn"] = data["RegisteredGatewayArn"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "Definition" in data:
        out["definition"] = data["Definition"]
    if "NameTag" in data:
        out["name_tag"] = data["NameTag"]
    if "IsMiddlebox" in data:
        out["is_middlebox"] = data["IsMiddlebox"]
    else:
        out["is_middlebox"] = False
    return out
