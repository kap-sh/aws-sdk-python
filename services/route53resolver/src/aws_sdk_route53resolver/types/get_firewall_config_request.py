"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetFirewallConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resource_id


class GetFirewallConfigRequest(TypedDict):
    resource_id: "aws_sdk_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the VPC from Amazon VPC that the configuration is for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFirewallConfigRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFirewallConfigRequest:
    out: GetFirewallConfigRequest = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("GetFirewallConfigRequest.resource_id required")
    return out
