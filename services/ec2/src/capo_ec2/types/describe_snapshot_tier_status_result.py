"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSnapshotTierStatusResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.snapshot_tier_status_set
    import capo_ec2.types.string


class DescribeSnapshotTierStatusResult(TypedDict, closed=True):
    snapshot_tier_statuses: NotRequired[
        "capo_ec2.types.snapshot_tier_status_set.snapshotTierStatusSet"
    ]
    """<p>Information about the snapshot's storage tier.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSnapshotTierStatusResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "snapshot_tier_statuses" in value:
        import capo_ec2.types.snapshot_tier_status_set

        capo_ec2.types.snapshot_tier_status_set.serialize_ec2_query(
            value["snapshot_tier_statuses"], pairs, f"{key_prefix}SnapshotTierStatusSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeSnapshotTierStatusResult:
    out: DescribeSnapshotTierStatusResult = {}  # type: ignore[typeddict-item]
    if el.find("SnapshotTierStatusSet") is not None:
        import capo_ec2.types.snapshot_tier_status_set

        out["snapshot_tier_statuses"] = (
            capo_ec2.types.snapshot_tier_status_set.deserialize_ec2_query(
                el, "SnapshotTierStatusSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
