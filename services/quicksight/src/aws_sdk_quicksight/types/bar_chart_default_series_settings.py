"""Generated from Smithy shape ``com.amazonaws.quicksight#BarChartDefaultSeriesSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.border_settings
    import aws_sdk_quicksight.types.decal_settings


class BarChartDefaultSeriesSettings(TypedDict):
    decal_settings: NotRequired["aws_sdk_quicksight.types.decal_settings.DecalSettings"]
    """<p>Decal settings for all bar series in the visual.</p>"""
    border_settings: NotRequired[
        "aws_sdk_quicksight.types.border_settings.BorderSettings"
    ]
    """<p>Border settings for all bar series in the visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BarChartDefaultSeriesSettings) -> dict:
    out: dict = {}
    if "decal_settings" in value:
        import aws_sdk_quicksight.types.decal_settings

        out["DecalSettings"] = aws_sdk_quicksight.types.decal_settings.serialize_json(
            value["decal_settings"]
        )
    if "border_settings" in value:
        import aws_sdk_quicksight.types.border_settings

        out["BorderSettings"] = aws_sdk_quicksight.types.border_settings.serialize_json(
            value["border_settings"]
        )
    return out


def deserialize_json(data: dict) -> BarChartDefaultSeriesSettings:
    out: BarChartDefaultSeriesSettings = {}  # type: ignore[typeddict-item]
    if "DecalSettings" in data:
        import aws_sdk_quicksight.types.decal_settings

        out["decal_settings"] = (
            aws_sdk_quicksight.types.decal_settings.deserialize_json(
                data["DecalSettings"]
            )
        )
    if "BorderSettings" in data:
        import aws_sdk_quicksight.types.border_settings

        out["border_settings"] = (
            aws_sdk_quicksight.types.border_settings.deserialize_json(
                data["BorderSettings"]
            )
        )
    return out
