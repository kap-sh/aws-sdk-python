"""Generated from Smithy shape ``com.amazonaws.dataexchange#S3SnapshotAsset``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__double_min0


class S3SnapshotAsset(TypedDict, closed=True):
    size: "capo_dataexchange.types.__double_min0.__doubleMin0"
    """<p>The size of the Amazon S3 object that is the object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3SnapshotAsset) -> dict:
    out: dict = {}
    out["Size"] = value.get("size", 0)
    return out


def deserialize_json(data: dict) -> S3SnapshotAsset:
    out: S3SnapshotAsset = {}  # type: ignore[typeddict-item]
    if "Size" in data:
        out["size"] = data["Size"]
    else:
        out["size"] = 0
    return out
