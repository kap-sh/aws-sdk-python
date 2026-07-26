"""Generated from Smithy shape ``com.amazonaws.guardduty#EbsSnapshotDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class EbsSnapshotDetails(TypedDict, closed=True):
    snapshot_arn: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the EBS snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EbsSnapshotDetails) -> dict:
    out: dict = {}
    if "snapshot_arn" in value:
        out["snapshotArn"] = value["snapshot_arn"]
    return out


def deserialize_json(data: dict) -> EbsSnapshotDetails:
    out: EbsSnapshotDetails = {}  # type: ignore[typeddict-item]
    if "snapshotArn" in data:
        out["snapshot_arn"] = data["snapshotArn"]
    return out
