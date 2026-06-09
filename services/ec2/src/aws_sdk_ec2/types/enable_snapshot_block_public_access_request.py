"""Generated from Smithy shape ``com.amazonaws.ec2#EnableSnapshotBlockPublicAccessRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.snapshot_block_public_access_state


class EnableSnapshotBlockPublicAccessRequest(TypedDict):
    state: NotRequired[
        "aws_sdk_ec2.types.snapshot_block_public_access_state.SnapshotBlockPublicAccessState"
    ]
    """<p>The mode in which to enable block public access for snapshots for the Region. Specify one of the following values:</p> <ul> <li> <p> <code>block-all-sharing</code> - Prevents all public sharing of snapshots in the Region. Users in the account will no longer be able to request new public sharing. Additionally, snapshots that are already publicly shared are treated as private and they are no longer publicly available.</p> </li> <li> <p> <code>block-new-sharing</code> - Prevents only new public sharing of snapshots in the Region. Users in the account will no longer be able to request new public sharing. However, snapshots that are already publicly shared, remain publicly available.</p> </li> </ul> <p> <code>unblocked</code> is not a valid value for <b>EnableSnapshotBlockPublicAccess</b>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableSnapshotBlockPublicAccessRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "state" in value:
        import aws_sdk_ec2.types.snapshot_block_public_access_state

        aws_sdk_ec2.types.snapshot_block_public_access_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> EnableSnapshotBlockPublicAccessRequest:
    out: EnableSnapshotBlockPublicAccessRequest = {}  # type: ignore[typeddict-item]
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.snapshot_block_public_access_state

        out["state"] = (
            aws_sdk_ec2.types.snapshot_block_public_access_state.deserialize_ec2_query(
                child_state
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
