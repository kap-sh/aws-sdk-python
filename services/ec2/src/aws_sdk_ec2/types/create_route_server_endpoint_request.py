"""Generated from Smithy shape ``com.amazonaws.ec2#CreateRouteServerEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.route_server_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id
    import aws_sdk_ec2.types.tag_specification_list


class CreateRouteServerEndpointRequest(TypedDict):
    route_server_id: NotRequired["aws_sdk_ec2.types.route_server_id.RouteServerId"]
    """<p>The ID of the route server for which to create an endpoint.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet in which to create the route server endpoint.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the route server endpoint during creation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateRouteServerEndpointRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "route_server_id" in value:
        pairs.append((f"{prefix}.RouteServerId", str(value["route_server_id"])))
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "tag_specifications" in value:
        import aws_sdk_ec2.types.tag_specification_list

        aws_sdk_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )


def deserialize_ec2_query(el: Element) -> CreateRouteServerEndpointRequest:
    out: CreateRouteServerEndpointRequest = {}  # type: ignore[typeddict-item]
    child_route_server_id = el.find("RouteServerId")
    if child_route_server_id is not None:
        out["route_server_id"] = str(child_route_server_id.text or "")
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("TagSpecifications") is not None:
        import aws_sdk_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            aws_sdk_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    return out
