"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteFleetsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.fleet_id_set


class DeleteFleetsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    fleet_ids: NotRequired["aws_sdk_ec2.types.fleet_id_set.FleetIdSet"]
    """<p>The IDs of the EC2 Fleets.</p> <p>Constraints: In a single request, you can specify up to 25 <code>instant</code> fleet IDs and up to 100 <code>maintain</code> or <code>request</code> fleet IDs. </p>"""
    terminate_instances: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to terminate the associated instances when the EC2 Fleet is deleted. The default is to terminate the instances.</p> <p>To let the instances continue to run after the EC2 Fleet is deleted, specify <code>no-terminate-instances</code>. Supported only for fleets of type <code>maintain</code> and <code>request</code>.</p> <p>For <code>instant</code> fleets, you cannot specify <code>NoTerminateInstances</code>. A deleted <code>instant</code> fleet with running instances is not supported.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteFleetsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "fleet_ids" in value:
        import aws_sdk_ec2.types.fleet_id_set

        aws_sdk_ec2.types.fleet_id_set.serialize_ec2_query(
            value["fleet_ids"], pairs, f"{prefix}.FleetIds"
        )
    if "terminate_instances" in value:
        pairs.append(
            (
                f"{prefix}.TerminateInstances",
                "true" if value["terminate_instances"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> DeleteFleetsRequest:
    out: DeleteFleetsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("FleetIds") is not None:
        import aws_sdk_ec2.types.fleet_id_set

        out["fleet_ids"] = aws_sdk_ec2.types.fleet_id_set.deserialize_ec2_query(
            el, "FleetIds"
        )
    child_terminate_instances = el.find("TerminateInstances")
    if child_terminate_instances is not None:
        out["terminate_instances"] = (
            child_terminate_instances.text or ""
        ).lower() == "true"
    return out
