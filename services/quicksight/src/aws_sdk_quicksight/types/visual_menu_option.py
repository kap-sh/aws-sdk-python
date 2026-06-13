"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualMenuOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dashboard_behavior


class VisualMenuOption(TypedDict):
    availability_status: NotRequired[
        "aws_sdk_quicksight.types.dashboard_behavior.DashboardBehavior"
    ]
    """<p>The availaiblity status of a visual's menu options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisualMenuOption) -> dict:
    out: dict = {}
    if "availability_status" in value:
        import aws_sdk_quicksight.types.dashboard_behavior

        out["AvailabilityStatus"] = (
            aws_sdk_quicksight.types.dashboard_behavior.serialize_json(
                value["availability_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> VisualMenuOption:
    out: VisualMenuOption = {}  # type: ignore[typeddict-item]
    if "AvailabilityStatus" in data:
        import aws_sdk_quicksight.types.dashboard_behavior

        out["availability_status"] = (
            aws_sdk_quicksight.types.dashboard_behavior.deserialize_json(
                data["AvailabilityStatus"]
            )
        )
    return out
