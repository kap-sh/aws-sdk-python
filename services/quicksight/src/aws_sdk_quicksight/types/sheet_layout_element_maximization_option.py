"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetLayoutElementMaximizationOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dashboard_behavior


class SheetLayoutElementMaximizationOption(TypedDict):
    availability_status: NotRequired[
        "aws_sdk_quicksight.types.dashboard_behavior.DashboardBehavior"
    ]
    """<p>The status of the sheet layout maximization options of a dashbaord.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetLayoutElementMaximizationOption) -> dict:
    out: dict = {}
    if "availability_status" in value:
        import aws_sdk_quicksight.types.dashboard_behavior

        out["AvailabilityStatus"] = (
            aws_sdk_quicksight.types.dashboard_behavior.serialize_json(
                value["availability_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> SheetLayoutElementMaximizationOption:
    out: SheetLayoutElementMaximizationOption = {}  # type: ignore[typeddict-item]
    if "AvailabilityStatus" in data:
        import aws_sdk_quicksight.types.dashboard_behavior

        out["availability_status"] = (
            aws_sdk_quicksight.types.dashboard_behavior.deserialize_json(
                data["AvailabilityStatus"]
            )
        )
    return out
