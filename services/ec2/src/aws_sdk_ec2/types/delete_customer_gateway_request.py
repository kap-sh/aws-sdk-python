"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteCustomerGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.customer_gateway_id


class DeleteCustomerGatewayRequest(TypedDict, closed=True):
    customer_gateway_id: NotRequired[
        "aws_sdk_ec2.types.customer_gateway_id.CustomerGatewayId"
    ]
    """<p>The ID of the customer gateway.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteCustomerGatewayRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "customer_gateway_id" in value:
        pairs.append((f"{prefix}.CustomerGatewayId", str(value["customer_gateway_id"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DeleteCustomerGatewayRequest:
    out: DeleteCustomerGatewayRequest = {}  # type: ignore[typeddict-item]
    child_customer_gateway_id = el.find("CustomerGatewayId")
    if child_customer_gateway_id is not None:
        out["customer_gateway_id"] = str(child_customer_gateway_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
