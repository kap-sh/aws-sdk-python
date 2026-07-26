"""Generated from Smithy shape ``com.amazonaws.quicksight#ExportWithHiddenFieldsOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dashboard_behavior


class ExportWithHiddenFieldsOption(TypedDict, closed=True):
    availability_status: NotRequired[
        "capo_quicksight.types.dashboard_behavior.DashboardBehavior"
    ]
    """<p>The status of the export with hidden fields options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportWithHiddenFieldsOption) -> dict:
    out: dict = {}
    if "availability_status" in value:
        import capo_quicksight.types.dashboard_behavior

        out["AvailabilityStatus"] = (
            capo_quicksight.types.dashboard_behavior.serialize_json(
                value["availability_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExportWithHiddenFieldsOption:
    out: ExportWithHiddenFieldsOption = {}  # type: ignore[typeddict-item]
    if "AvailabilityStatus" in data:
        import capo_quicksight.types.dashboard_behavior

        out["availability_status"] = (
            capo_quicksight.types.dashboard_behavior.deserialize_json(
                data["AvailabilityStatus"]
            )
        )
    return out
