"""Generated from Smithy shape ``com.amazonaws.quicksight#ThemeVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.resource_status
    import capo_quicksight.types.timestamp
    import capo_quicksight.types.version_description
    import capo_quicksight.types.version_number


class ThemeVersionSummary(TypedDict, closed=True):
    version_number: NotRequired["capo_quicksight.types.version_number.VersionNumber"]
    """<p>The version number of the theme version.</p>"""
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the theme version.</p>"""
    description: NotRequired[
        "capo_quicksight.types.version_description.VersionDescription"
    ]
    """<p>The description of the theme version.</p>"""
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The date and time that this theme version was created.</p>"""
    status: NotRequired["capo_quicksight.types.resource_status.ResourceStatus"]
    """<p>The status of the theme version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThemeVersionSummary) -> dict:
    out: dict = {}
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "status" in value:
        import capo_quicksight.types.resource_status

        out["Status"] = capo_quicksight.types.resource_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> ThemeVersionSummary:
    out: ThemeVersionSummary = {}  # type: ignore[typeddict-item]
    if "VersionNumber" in data:
        out["version_number"] = data["VersionNumber"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedTime" in data:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "Status" in data:
        import capo_quicksight.types.resource_status

        out["status"] = capo_quicksight.types.resource_status.deserialize_json(
            data["Status"]
        )
    return out
