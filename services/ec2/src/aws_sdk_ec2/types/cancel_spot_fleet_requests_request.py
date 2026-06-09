"""Generated from Smithy shape ``com.amazonaws.ec2#CancelSpotFleetRequestsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.spot_fleet_request_id_list


class CancelSpotFleetRequestsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    spot_fleet_request_ids: NotRequired[
        "aws_sdk_ec2.types.spot_fleet_request_id_list.SpotFleetRequestIdList"
    ]
    """<p>The IDs of the Spot Fleet requests.</p> <p>Constraint: You can specify up to 100 IDs in a single request.</p>"""
    terminate_instances: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to terminate the associated instances when the Spot Fleet request is canceled. The default is to terminate the instances.</p> <p>To let the instances continue to run after the Spot Fleet request is canceled, specify <code>no-terminate-instances</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelSpotFleetRequestsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "spot_fleet_request_ids" in value:
        import aws_sdk_ec2.types.spot_fleet_request_id_list

        aws_sdk_ec2.types.spot_fleet_request_id_list.serialize_ec2_query(
            value["spot_fleet_request_ids"], pairs, f"{prefix}.SpotFleetRequestId"
        )
    if "terminate_instances" in value:
        pairs.append(
            (
                f"{prefix}.TerminateInstances",
                "true" if value["terminate_instances"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> CancelSpotFleetRequestsRequest:
    out: CancelSpotFleetRequestsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("SpotFleetRequestId") is not None:
        import aws_sdk_ec2.types.spot_fleet_request_id_list

        out["spot_fleet_request_ids"] = (
            aws_sdk_ec2.types.spot_fleet_request_id_list.deserialize_ec2_query(
                el, "SpotFleetRequestId"
            )
        )
    child_terminate_instances = el.find("TerminateInstances")
    if child_terminate_instances is not None:
        out["terminate_instances"] = (
            child_terminate_instances.text or ""
        ).lower() == "true"
    return out
