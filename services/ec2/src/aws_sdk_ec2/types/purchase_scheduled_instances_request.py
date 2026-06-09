"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseScheduledInstancesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.purchase_request_set
    import aws_sdk_ec2.types.string


class PurchaseScheduledInstancesRequest(TypedDict):
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that ensures the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring Idempotency</a>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    purchase_requests: NotRequired[
        "aws_sdk_ec2.types.purchase_request_set.PurchaseRequestSet"
    ]
    """<p>The purchase requests.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PurchaseScheduledInstancesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "purchase_requests" in value:
        import aws_sdk_ec2.types.purchase_request_set

        aws_sdk_ec2.types.purchase_request_set.serialize_ec2_query(
            value["purchase_requests"], pairs, f"{prefix}.PurchaseRequests"
        )


def deserialize_ec2_query(el: Element) -> PurchaseScheduledInstancesRequest:
    out: PurchaseScheduledInstancesRequest = {}  # type: ignore[typeddict-item]
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("PurchaseRequests") is not None:
        import aws_sdk_ec2.types.purchase_request_set

        out["purchase_requests"] = (
            aws_sdk_ec2.types.purchase_request_set.deserialize_ec2_query(
                el, "PurchaseRequests"
            )
        )
    return out
