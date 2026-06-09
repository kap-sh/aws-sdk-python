"""Generated from Smithy shape ``com.amazonaws.ec2#CancelSpotInstanceRequestsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.spot_instance_request_id_list


class CancelSpotInstanceRequestsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    spot_instance_request_ids: NotRequired[
        "aws_sdk_ec2.types.spot_instance_request_id_list.SpotInstanceRequestIdList"
    ]
    """<p>The IDs of the Spot Instance requests.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelSpotInstanceRequestsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "spot_instance_request_ids" in value:
        import aws_sdk_ec2.types.spot_instance_request_id_list

        aws_sdk_ec2.types.spot_instance_request_id_list.serialize_ec2_query(
            value["spot_instance_request_ids"],
            pairs,
            f"{prefix}.SpotInstanceRequestIds",
        )


def deserialize_ec2_query(el: Element) -> CancelSpotInstanceRequestsRequest:
    out: CancelSpotInstanceRequestsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("SpotInstanceRequestIds") is not None:
        import aws_sdk_ec2.types.spot_instance_request_id_list

        out["spot_instance_request_ids"] = (
            aws_sdk_ec2.types.spot_instance_request_id_list.deserialize_ec2_query(
                el, "SpotInstanceRequestIds"
            )
        )
    return out
