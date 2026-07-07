"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashDvbSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.dash_dvb_error_metrics
    import aws_sdk_mediapackagev2.types.dash_dvb_font_download


class DashDvbSettings(TypedDict, closed=True):
    font_download: NotRequired[
        "aws_sdk_mediapackagev2.types.dash_dvb_font_download.DashDvbFontDownload"
    ]
    """<p>Subtitle font settings.</p>"""
    error_metrics: NotRequired[
        "aws_sdk_mediapackagev2.types.dash_dvb_error_metrics.DashDvbErrorMetrics"
    ]
    """<p>Playback device error reporting settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashDvbSettings) -> dict:
    out: dict = {}
    if "font_download" in value:
        import aws_sdk_mediapackagev2.types.dash_dvb_font_download

        out["FontDownload"] = (
            aws_sdk_mediapackagev2.types.dash_dvb_font_download.serialize_json(
                value["font_download"]
            )
        )
    if "error_metrics" in value:
        import aws_sdk_mediapackagev2.types.dash_dvb_error_metrics

        out["ErrorMetrics"] = (
            aws_sdk_mediapackagev2.types.dash_dvb_error_metrics.serialize_json(
                value["error_metrics"]
            )
        )
    return out


def deserialize_json(data: dict) -> DashDvbSettings:
    out: DashDvbSettings = {}  # type: ignore[typeddict-item]
    if "FontDownload" in data:
        import aws_sdk_mediapackagev2.types.dash_dvb_font_download

        out["font_download"] = (
            aws_sdk_mediapackagev2.types.dash_dvb_font_download.deserialize_json(
                data["FontDownload"]
            )
        )
    if "ErrorMetrics" in data:
        import aws_sdk_mediapackagev2.types.dash_dvb_error_metrics

        out["error_metrics"] = (
            aws_sdk_mediapackagev2.types.dash_dvb_error_metrics.deserialize_json(
                data["ErrorMetrics"]
            )
        )
    return out
