"""Generated from Smithy shape ``com.amazonaws.quicksight#DataPointTooltipOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dashboard_behavior


class DataPointTooltipOption(TypedDict):
    availability_status: NotRequired[
        "aws_sdk_quicksight.types.dashboard_behavior.DashboardBehavior"
    ]
    """<p>The status of the data point tool tip options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataPointTooltipOption) -> dict:
    out: dict = {}
    if "availability_status" in value:
        import aws_sdk_quicksight.types.dashboard_behavior

        out["AvailabilityStatus"] = (
            aws_sdk_quicksight.types.dashboard_behavior.serialize_json(
                value["availability_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataPointTooltipOption:
    out: DataPointTooltipOption = {}  # type: ignore[typeddict-item]
    if "AvailabilityStatus" in data:
        import aws_sdk_quicksight.types.dashboard_behavior

        out["availability_status"] = (
            aws_sdk_quicksight.types.dashboard_behavior.deserialize_json(
                data["AvailabilityStatus"]
            )
        )
    return out
