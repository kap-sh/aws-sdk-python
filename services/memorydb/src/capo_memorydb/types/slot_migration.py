"""Generated from Smithy shape ``com.amazonaws.memorydb#SlotMigration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.double


class SlotMigration(TypedDict, closed=True):
    progress_percentage: "capo_memorydb.types.double.Double"
    """<p>The percentage of the slot migration that is complete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SlotMigration) -> dict:
    out: dict = {}
    out["ProgressPercentage"] = value.get("progress_percentage", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> SlotMigration:
    out: SlotMigration = {}  # type: ignore[typeddict-item]
    if "ProgressPercentage" in data:
        out["progress_percentage"] = data["ProgressPercentage"]
    else:
        out["progress_percentage"] = 0
    return out
