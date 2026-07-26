"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualAxisSortOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dashboard_behavior


class VisualAxisSortOption(TypedDict, closed=True):
    availability_status: NotRequired[
        "capo_quicksight.types.dashboard_behavior.DashboardBehavior"
    ]
    """<p>The availaiblity status of a visual's axis sort options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisualAxisSortOption) -> dict:
    out: dict = {}
    if "availability_status" in value:
        import capo_quicksight.types.dashboard_behavior

        out["AvailabilityStatus"] = (
            capo_quicksight.types.dashboard_behavior.serialize_json(
                value["availability_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> VisualAxisSortOption:
    out: VisualAxisSortOption = {}  # type: ignore[typeddict-item]
    if "AvailabilityStatus" in data:
        import capo_quicksight.types.dashboard_behavior

        out["availability_status"] = (
            capo_quicksight.types.dashboard_behavior.deserialize_json(
                data["AvailabilityStatus"]
            )
        )
    return out
