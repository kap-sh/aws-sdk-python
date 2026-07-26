"""Generated from Smithy shape ``com.amazonaws.quicksight#ThemeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.theme_name
    import capo_quicksight.types.timestamp
    import capo_quicksight.types.version_number


class ThemeSummary(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    name: NotRequired["capo_quicksight.types.theme_name.ThemeName"]
    """<p>the display name for the theme.</p>"""
    theme_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the theme. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    latest_version_number: NotRequired[
        "capo_quicksight.types.version_number.VersionNumber"
    ]
    """<p>The latest version number for the theme. </p>"""
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The date and time that this theme was created.</p>"""
    last_updated_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The last date and time that this theme was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThemeSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "theme_id" in value:
        out["ThemeId"] = value["theme_id"]
    if "latest_version_number" in value:
        out["LatestVersionNumber"] = value["latest_version_number"]
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import capo_quicksight.types.timestamp

        out["LastUpdatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    return out


def deserialize_json(data: dict) -> ThemeSummary:
    out: ThemeSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ThemeId" in data:
        out["theme_id"] = data["ThemeId"]
    if "LatestVersionNumber" in data:
        out["latest_version_number"] = data["LatestVersionNumber"]
    if "CreatedTime" in data:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastUpdatedTime" in data:
        import capo_quicksight.types.timestamp

        out["last_updated_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    return out
