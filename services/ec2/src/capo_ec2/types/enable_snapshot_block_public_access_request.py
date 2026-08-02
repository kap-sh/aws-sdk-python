"""Generated from Smithy shape ``com.amazonaws.ec2#EnableSnapshotBlockPublicAccessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.snapshot_block_public_access_state


class EnableSnapshotBlockPublicAccessRequest(TypedDict, closed=True):
    state: NotRequired[
        "capo_ec2.types.snapshot_block_public_access_state.SnapshotBlockPublicAccessState"
    ]
    """<p>The mode in which to enable block public access for snapshots for the Region. Specify one of the following values:</p> <ul> <li> <p> <code>block-all-sharing</code> - Prevents all public sharing of snapshots in the Region. Users in the account will no longer be able to request new public sharing. Additionally, snapshots that are already publicly shared are treated as private and they are no longer publicly available.</p> </li> <li> <p> <code>block-new-sharing</code> - Prevents only new public sharing of snapshots in the Region. Users in the account will no longer be able to request new public sharing. However, snapshots that are already publicly shared, remain publicly available.</p> </li> </ul> <p> <code>unblocked</code> is not a valid value for <b>EnableSnapshotBlockPublicAccess</b>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableSnapshotBlockPublicAccessRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "state" in value:
        import capo_ec2.types.snapshot_block_public_access_state

        capo_ec2.types.snapshot_block_public_access_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> EnableSnapshotBlockPublicAccessRequest:
    out: EnableSnapshotBlockPublicAccessRequest = {}  # type: ignore[typeddict-item]
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.snapshot_block_public_access_state

        out["state"] = (
            capo_ec2.types.snapshot_block_public_access_state.deserialize_ec2_query(
                child_state
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
