"""Generated from Smithy shape ``com.amazonaws.quicksight#BarChartDefaultSeriesSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.border_settings
    import capo_quicksight.types.decal_settings


class BarChartDefaultSeriesSettings(TypedDict, closed=True):
    decal_settings: NotRequired["capo_quicksight.types.decal_settings.DecalSettings"]
    """<p>Decal settings for all bar series in the visual.</p>"""
    border_settings: NotRequired["capo_quicksight.types.border_settings.BorderSettings"]
    """<p>Border settings for all bar series in the visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BarChartDefaultSeriesSettings) -> dict:
    out: dict = {}
    if "decal_settings" in value:
        import capo_quicksight.types.decal_settings

        out["DecalSettings"] = capo_quicksight.types.decal_settings.serialize_json(
            value["decal_settings"]
        )
    if "border_settings" in value:
        import capo_quicksight.types.border_settings

        out["BorderSettings"] = capo_quicksight.types.border_settings.serialize_json(
            value["border_settings"]
        )
    return out


def deserialize_json(data: dict) -> BarChartDefaultSeriesSettings:
    out: BarChartDefaultSeriesSettings = {}  # type: ignore[typeddict-item]
    if "DecalSettings" in data:
        import capo_quicksight.types.decal_settings

        out["decal_settings"] = capo_quicksight.types.decal_settings.deserialize_json(
            data["DecalSettings"]
        )
    if "BorderSettings" in data:
        import capo_quicksight.types.border_settings

        out["border_settings"] = capo_quicksight.types.border_settings.deserialize_json(
            data["BorderSettings"]
        )
    return out
