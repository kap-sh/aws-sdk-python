"""Generated from Smithy shape ``com.amazonaws.ec2#ListSnapshotsInRecycleBinResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.snapshot_recycle_bin_info_list
    import aws_sdk_ec2.types.string


class ListSnapshotsInRecycleBinResult(TypedDict):
    snapshots: NotRequired[
        "aws_sdk_ec2.types.snapshot_recycle_bin_info_list.SnapshotRecycleBinInfoList"
    ]
    """<p>Information about the snapshots.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ListSnapshotsInRecycleBinResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "snapshots" in value:
        import aws_sdk_ec2.types.snapshot_recycle_bin_info_list

        aws_sdk_ec2.types.snapshot_recycle_bin_info_list.serialize_ec2_query(
            value["snapshots"], pairs, f"{prefix}.SnapshotSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> ListSnapshotsInRecycleBinResult:
    out: ListSnapshotsInRecycleBinResult = {}  # type: ignore[typeddict-item]
    if el.find("SnapshotSet") is not None:
        import aws_sdk_ec2.types.snapshot_recycle_bin_info_list

        out["snapshots"] = (
            aws_sdk_ec2.types.snapshot_recycle_bin_info_list.deserialize_ec2_query(
                el, "SnapshotSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
