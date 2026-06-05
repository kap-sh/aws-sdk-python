"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFastSnapshotRestoresResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_fast_snapshot_restore_success_set
    import aws_sdk_ec2.types.next_token


class DescribeFastSnapshotRestoresResult(TypedDict):
    fast_snapshot_restores: NotRequired[
        "aws_sdk_ec2.types.describe_fast_snapshot_restore_success_set.DescribeFastSnapshotRestoreSuccessSet"
    ]
    """<p>Information about the state of fast snapshot restores.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeFastSnapshotRestoresResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "fast_snapshot_restores" in value:
        import aws_sdk_ec2.types.describe_fast_snapshot_restore_success_set

        aws_sdk_ec2.types.describe_fast_snapshot_restore_success_set.serialize_ec2_query(
            value["fast_snapshot_restores"], pairs, f"{prefix}.FastSnapshotRestoreSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeFastSnapshotRestoresResult:
    out: DescribeFastSnapshotRestoresResult = {}  # type: ignore[typeddict-item]
    if el.find("FastSnapshotRestoreSet") is not None:
        import aws_sdk_ec2.types.describe_fast_snapshot_restore_success_set

        out["fast_snapshot_restores"] = (
            aws_sdk_ec2.types.describe_fast_snapshot_restore_success_set.deserialize_ec2_query(
                el, "FastSnapshotRestoreSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
