"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteInternetGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.internet_gateway_id


class DeleteInternetGatewayRequest(TypedDict, closed=True):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    internet_gateway_id: NotRequired[
        "aws_sdk_ec2.types.internet_gateway_id.InternetGatewayId"
    ]
    """<p>The ID of the internet gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteInternetGatewayRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "internet_gateway_id" in value:
        pairs.append((f"{prefix}.InternetGatewayId", str(value["internet_gateway_id"])))


def deserialize_ec2_query(el: Element) -> DeleteInternetGatewayRequest:
    out: DeleteInternetGatewayRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_internet_gateway_id = el.find("InternetGatewayId")
    if child_internet_gateway_id is not None:
        out["internet_gateway_id"] = str(child_internet_gateway_id.text or "")
    return out
