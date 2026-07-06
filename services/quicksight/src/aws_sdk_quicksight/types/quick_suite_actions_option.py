"""Generated from Smithy shape ``com.amazonaws.quicksight#QuickSuiteActionsOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dashboard_behavior


class QuickSuiteActionsOption(TypedDict, closed=True):
    availability_status: NotRequired[
        "aws_sdk_quicksight.types.dashboard_behavior.DashboardBehavior"
    ]
    """<p>Availability status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuickSuiteActionsOption) -> dict:
    out: dict = {}
    if "availability_status" in value:
        import aws_sdk_quicksight.types.dashboard_behavior

        out["AvailabilityStatus"] = (
            aws_sdk_quicksight.types.dashboard_behavior.serialize_json(
                value["availability_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> QuickSuiteActionsOption:
    out: QuickSuiteActionsOption = {}  # type: ignore[typeddict-item]
    if "AvailabilityStatus" in data:
        import aws_sdk_quicksight.types.dashboard_behavior

        out["availability_status"] = (
            aws_sdk_quicksight.types.dashboard_behavior.deserialize_json(
                data["AvailabilityStatus"]
            )
        )
    return out
