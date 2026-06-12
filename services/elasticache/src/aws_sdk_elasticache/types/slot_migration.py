"""Generated from Smithy shape ``com.amazonaws.elasticache#SlotMigration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.double


class SlotMigration(TypedDict):
    progress_percentage: NotRequired["aws_sdk_elasticache.types.double.Double"]
    """<p>The percentage of the slot migration that is complete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SlotMigration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "progress_percentage" in value:
        pairs.append(
            (f"{prefix}.ProgressPercentage", str(value["progress_percentage"]))
        )


def deserialize_query(el: Element) -> SlotMigration:
    out: SlotMigration = {}  # type: ignore[typeddict-item]
    child_progress_percentage = el.find("ProgressPercentage")
    if child_progress_percentage is not None:
        out["progress_percentage"] = float(child_progress_percentage.text or "")
    return out
