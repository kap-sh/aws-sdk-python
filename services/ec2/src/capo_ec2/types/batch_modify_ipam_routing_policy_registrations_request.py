"""Generated from Smithy shape ``com.amazonaws.ec2#BatchModifyIpamRoutingPolicyRegistrationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.boxed_boolean
    import capo_ec2.types.ipam_internet_registry_association_id
    import capo_ec2.types.string


class BatchModifyIpamRoutingPolicyRegistrationsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_internet_registry_association_id: NotRequired[
        "capo_ec2.types.ipam_internet_registry_association_id.IpamInternetRegistryAssociationId"
    ]
    """<p>The ID of the IPAM internet registry association.</p>"""
    delta_json: NotRequired["capo_ec2.types.string.String"]
    """<p>The batch modifications to apply, in JSON format.</p>"""
    force: NotRequired["capo_ec2.types.boxed_boolean.BoxedBoolean"]
    """<p>Forces the batch modification even if individual changes conflict with announced routes. Default: <code>false</code>.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the operation ignores the request, but does not return an error.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: BatchModifyIpamRoutingPolicyRegistrationsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_internet_registry_association_id" in value:
        pairs.append(
            (
                f"{key_prefix}IpamInternetRegistryAssociationId",
                str(value["ipam_internet_registry_association_id"]),
            )
        )
    if "delta_json" in value:
        pairs.append((f"{key_prefix}DeltaJson", str(value["delta_json"])))
    if "force" in value:
        pairs.append((f"{key_prefix}Force", "true" if value["force"] else "false"))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))


def deserialize_ec2_query(
    el: Element,
) -> BatchModifyIpamRoutingPolicyRegistrationsRequest:
    out: BatchModifyIpamRoutingPolicyRegistrationsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_internet_registry_association_id = el.find(
        "IpamInternetRegistryAssociationId"
    )
    if child_ipam_internet_registry_association_id is not None:
        out["ipam_internet_registry_association_id"] = str(
            child_ipam_internet_registry_association_id.text or ""
        )
    child_delta_json = el.find("DeltaJson")
    if child_delta_json is not None:
        out["delta_json"] = str(child_delta_json.text or "")
    child_force = el.find("Force")
    if child_force is not None:
        out["force"] = (child_force.text or "").lower() == "true"
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
