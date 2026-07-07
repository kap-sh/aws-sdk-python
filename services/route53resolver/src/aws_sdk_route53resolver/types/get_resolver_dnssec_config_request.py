"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetResolverDnssecConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resource_id


class GetResolverDnssecConfigRequest(TypedDict, closed=True):
    resource_id: "aws_sdk_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the virtual private cloud (VPC) for the DNSSEC validation status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResolverDnssecConfigRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResolverDnssecConfigRequest:
    out: GetResolverDnssecConfigRequest = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError(
            "GetResolverDnssecConfigRequest.resource_id required"
        )
    return out
