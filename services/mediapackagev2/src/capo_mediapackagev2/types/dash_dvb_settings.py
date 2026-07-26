"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashDvbSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.dash_dvb_error_metrics
    import capo_mediapackagev2.types.dash_dvb_font_download


class DashDvbSettings(TypedDict, closed=True):
    font_download: NotRequired[
        "capo_mediapackagev2.types.dash_dvb_font_download.DashDvbFontDownload"
    ]
    """<p>Subtitle font settings.</p>"""
    error_metrics: NotRequired[
        "capo_mediapackagev2.types.dash_dvb_error_metrics.DashDvbErrorMetrics"
    ]
    """<p>Playback device error reporting settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashDvbSettings) -> dict:
    out: dict = {}
    if "font_download" in value:
        import capo_mediapackagev2.types.dash_dvb_font_download

        out["FontDownload"] = (
            capo_mediapackagev2.types.dash_dvb_font_download.serialize_json(
                value["font_download"]
            )
        )
    if "error_metrics" in value:
        import capo_mediapackagev2.types.dash_dvb_error_metrics

        out["ErrorMetrics"] = (
            capo_mediapackagev2.types.dash_dvb_error_metrics.serialize_json(
                value["error_metrics"]
            )
        )
    return out


def deserialize_json(data: dict) -> DashDvbSettings:
    out: DashDvbSettings = {}  # type: ignore[typeddict-item]
    if "FontDownload" in data:
        import capo_mediapackagev2.types.dash_dvb_font_download

        out["font_download"] = (
            capo_mediapackagev2.types.dash_dvb_font_download.deserialize_json(
                data["FontDownload"]
            )
        )
    if "ErrorMetrics" in data:
        import capo_mediapackagev2.types.dash_dvb_error_metrics

        out["error_metrics"] = (
            capo_mediapackagev2.types.dash_dvb_error_metrics.deserialize_json(
                data["ErrorMetrics"]
            )
        )
    return out
