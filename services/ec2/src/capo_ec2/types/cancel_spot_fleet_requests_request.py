"""Generated from Smithy shape ``com.amazonaws.ec2#CancelSpotFleetRequestsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.spot_fleet_request_id_list


class CancelSpotFleetRequestsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    spot_fleet_request_ids: NotRequired[
        "capo_ec2.types.spot_fleet_request_id_list.SpotFleetRequestIdList"
    ]
    """<p>The IDs of the Spot Fleet requests.</p> <p>Constraint: You can specify up to 100 IDs in a single request.</p>"""
    terminate_instances: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to terminate the associated instances when the Spot Fleet request is canceled. The default is to terminate the instances.</p> <p>To let the instances continue to run after the Spot Fleet request is canceled, specify <code>no-terminate-instances</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelSpotFleetRequestsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "spot_fleet_request_ids" in value:
        import capo_ec2.types.spot_fleet_request_id_list

        capo_ec2.types.spot_fleet_request_id_list.serialize_ec2_query(
            value["spot_fleet_request_ids"], pairs, f"{key_prefix}SpotFleetRequestId"
        )
    if "terminate_instances" in value:
        pairs.append(
            (
                f"{key_prefix}TerminateInstances",
                "true" if value["terminate_instances"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> CancelSpotFleetRequestsRequest:
    out: CancelSpotFleetRequestsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_spot_fleet_request_ids = el.find("spotFleetRequestId")
    if child_spot_fleet_request_ids is not None:
        import capo_ec2.types.spot_fleet_request_id_list

        out["spot_fleet_request_ids"] = (
            capo_ec2.types.spot_fleet_request_id_list.deserialize_ec2_query(
                child_spot_fleet_request_ids
            )
        )
    child_terminate_instances = el.find("terminateInstances")
    if child_terminate_instances is not None:
        out["terminate_instances"] = (
            child_terminate_instances.text or ""
        ).lower() == "true"
    return out
