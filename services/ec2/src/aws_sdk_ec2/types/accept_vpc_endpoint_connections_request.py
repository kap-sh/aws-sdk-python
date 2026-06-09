"""Generated from Smithy shape ``com.amazonaws.ec2#AcceptVpcEndpointConnectionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.vpc_endpoint_id_list
    import aws_sdk_ec2.types.vpc_endpoint_service_id


class AcceptVpcEndpointConnectionsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    service_id: NotRequired[
        "aws_sdk_ec2.types.vpc_endpoint_service_id.VpcEndpointServiceId"
    ]
    """<p>The ID of the VPC endpoint service.</p>"""
    vpc_endpoint_ids: NotRequired[
        "aws_sdk_ec2.types.vpc_endpoint_id_list.VpcEndpointIdList"
    ]
    """<p>The IDs of the interface VPC endpoints.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AcceptVpcEndpointConnectionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "service_id" in value:
        pairs.append((f"{prefix}.ServiceId", str(value["service_id"])))
    if "vpc_endpoint_ids" in value:
        import aws_sdk_ec2.types.vpc_endpoint_id_list

        aws_sdk_ec2.types.vpc_endpoint_id_list.serialize_ec2_query(
            value["vpc_endpoint_ids"], pairs, f"{prefix}.VpcEndpointIds"
        )


def deserialize_ec2_query(el: Element) -> AcceptVpcEndpointConnectionsRequest:
    out: AcceptVpcEndpointConnectionsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_service_id = el.find("ServiceId")
    if child_service_id is not None:
        out["service_id"] = str(child_service_id.text or "")
    if el.find("VpcEndpointIds") is not None:
        import aws_sdk_ec2.types.vpc_endpoint_id_list

        out["vpc_endpoint_ids"] = (
            aws_sdk_ec2.types.vpc_endpoint_id_list.deserialize_ec2_query(
                el, "VpcEndpointIds"
            )
        )
    return out
