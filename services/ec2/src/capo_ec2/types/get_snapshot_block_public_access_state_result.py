"""Generated from Smithy shape ``com.amazonaws.ec2#GetSnapshotBlockPublicAccessStateResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.managed_by
    import capo_ec2.types.snapshot_block_public_access_state


class GetSnapshotBlockPublicAccessStateResult(TypedDict, closed=True):
    state: NotRequired[
        "capo_ec2.types.snapshot_block_public_access_state.SnapshotBlockPublicAccessState"
    ]
    """<p>The current state of block public access for snapshots. Possible values include:</p> <ul> <li> <p> <code>block-all-sharing</code> - All public sharing of snapshots is blocked. Users in the account can't request new public sharing. Additionally, snapshots that were already publicly shared are treated as private and are not publicly available.</p> </li> <li> <p> <code>block-new-sharing</code> - Only new public sharing of snapshots is blocked. Users in the account can't request new public sharing. However, snapshots that were already publicly shared, remain publicly available.</p> </li> <li> <p> <code>unblocked</code> - Public sharing is not blocked. Users can publicly share snapshots.</p> </li> </ul>"""
    managed_by: NotRequired["capo_ec2.types.managed_by.ManagedBy"]
    """<p>The entity that manages the state for block public access for snapshots. Possible values include:</p> <ul> <li> <p> <code>account</code> - The state is managed by the account.</p> </li> <li> <p> <code>declarative-policy</code> - The state is managed by a declarative policy and can't be modified by the account.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetSnapshotBlockPublicAccessStateResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "state" in value:
        import capo_ec2.types.snapshot_block_public_access_state

        capo_ec2.types.snapshot_block_public_access_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "managed_by" in value:
        import capo_ec2.types.managed_by

        capo_ec2.types.managed_by.serialize_ec2_query(
            value["managed_by"], pairs, f"{key_prefix}ManagedBy"
        )


def deserialize_ec2_query(el: Element) -> GetSnapshotBlockPublicAccessStateResult:
    out: GetSnapshotBlockPublicAccessStateResult = {}  # type: ignore[typeddict-item]
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.snapshot_block_public_access_state

        out["state"] = (
            capo_ec2.types.snapshot_block_public_access_state.deserialize_ec2_query(
                child_state
            )
        )
    child_managed_by = el.find("managedBy")
    if child_managed_by is not None:
        import capo_ec2.types.managed_by

        out["managed_by"] = capo_ec2.types.managed_by.deserialize_ec2_query(
            child_managed_by
        )
    return out
