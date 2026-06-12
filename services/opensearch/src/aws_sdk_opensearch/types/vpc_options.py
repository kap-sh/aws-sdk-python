"""Generated from Smithy shape ``com.amazonaws.opensearch#VPCOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.string_list


class VPCOptions(TypedDict):
    subnet_ids: NotRequired["aws_sdk_opensearch.types.string_list.StringList"]
    """<p>A list of subnet IDs associated with the VPC endpoints for the domain. If your domain uses multiple Availability Zones, you need to provide two subnet IDs, one per zone. Otherwise, provide only one.</p>"""
    security_group_ids: NotRequired["aws_sdk_opensearch.types.string_list.StringList"]
    """<p>The list of security group IDs associated with the VPC endpoints for the domain. If you do not provide a security group ID, OpenSearch Service uses the default security group for the VPC.</p>"""
    egress_enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Controls whether egress traffic from the domain is routed through the customer VPC. When <code>true</code>, outbound traffic flows through the VPC. When <code>false</code>, outbound traffic goes through the public internet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VPCOptions) -> dict:
    out: dict = {}
    if "subnet_ids" in value:
        import aws_sdk_opensearch.types.string_list

        out["SubnetIds"] = aws_sdk_opensearch.types.string_list.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import aws_sdk_opensearch.types.string_list

        out["SecurityGroupIds"] = aws_sdk_opensearch.types.string_list.serialize_json(
            value["security_group_ids"]
        )
    if "egress_enabled" in value:
        out["EgressEnabled"] = value["egress_enabled"]
    return out


def deserialize_json(data: dict) -> VPCOptions:
    out: VPCOptions = {}  # type: ignore[typeddict-item]
    if "SubnetIds" in data:
        import aws_sdk_opensearch.types.string_list

        out["subnet_ids"] = aws_sdk_opensearch.types.string_list.deserialize_json(
            data["SubnetIds"]
        )
    if "SecurityGroupIds" in data:
        import aws_sdk_opensearch.types.string_list

        out["security_group_ids"] = (
            aws_sdk_opensearch.types.string_list.deserialize_json(
                data["SecurityGroupIds"]
            )
        )
    if "EgressEnabled" in data:
        out["egress_enabled"] = data["EgressEnabled"]
    return out
