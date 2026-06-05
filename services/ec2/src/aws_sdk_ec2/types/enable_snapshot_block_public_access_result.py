"""Generated from Smithy shape ``com.amazonaws.ec2#EnableSnapshotBlockPublicAccessResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.snapshot_block_public_access_state


class EnableSnapshotBlockPublicAccessResult(TypedDict):
    state: NotRequired[
        "aws_sdk_ec2.types.snapshot_block_public_access_state.SnapshotBlockPublicAccessState"
    ]
    """<p>The state of block public access for snapshots for the account and Region. Returns either <code>block-all-sharing</code> or <code>block-new-sharing</code> if the request succeeds.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableSnapshotBlockPublicAccessResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "state" in value:
        import aws_sdk_ec2.types.snapshot_block_public_access_state

        aws_sdk_ec2.types.snapshot_block_public_access_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )


def deserialize_ec2_query(el: Element) -> EnableSnapshotBlockPublicAccessResult:
    out: EnableSnapshotBlockPublicAccessResult = {}  # type: ignore[typeddict-item]
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.snapshot_block_public_access_state

        out["state"] = (
            aws_sdk_ec2.types.snapshot_block_public_access_state.deserialize_ec2_query(
                child_state
            )
        )
    return out
