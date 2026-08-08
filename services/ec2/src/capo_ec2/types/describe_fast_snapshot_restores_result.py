"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFastSnapshotRestoresResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.describe_fast_snapshot_restore_success_set
    import capo_ec2.types.next_token


class DescribeFastSnapshotRestoresResult(TypedDict, closed=True):
    fast_snapshot_restores: NotRequired[
        "capo_ec2.types.describe_fast_snapshot_restore_success_set.DescribeFastSnapshotRestoreSuccessSet"
    ]
    """<p>Information about the state of fast snapshot restores.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeFastSnapshotRestoresResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "fast_snapshot_restores" in value:
        import capo_ec2.types.describe_fast_snapshot_restore_success_set

        capo_ec2.types.describe_fast_snapshot_restore_success_set.serialize_ec2_query(
            value["fast_snapshot_restores"],
            pairs,
            f"{key_prefix}FastSnapshotRestoreSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeFastSnapshotRestoresResult:
    out: DescribeFastSnapshotRestoresResult = {}  # type: ignore[typeddict-item]
    if el.find("fastSnapshotRestoreSet") is not None:
        import capo_ec2.types.describe_fast_snapshot_restore_success_set

        out["fast_snapshot_restores"] = (
            capo_ec2.types.describe_fast_snapshot_restore_success_set.deserialize_ec2_query(
                el, "fastSnapshotRestoreSet"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
