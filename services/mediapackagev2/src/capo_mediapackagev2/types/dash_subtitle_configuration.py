"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashSubtitleConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.dash_ttml_configuration


class DashSubtitleConfiguration(TypedDict, closed=True):
    ttml_configuration: NotRequired[
        "capo_mediapackagev2.types.dash_ttml_configuration.DashTtmlConfiguration"
    ]
    """<p>Settings for TTML subtitles.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashSubtitleConfiguration) -> dict:
    out: dict = {}
    if "ttml_configuration" in value:
        import capo_mediapackagev2.types.dash_ttml_configuration

        out["TtmlConfiguration"] = (
            capo_mediapackagev2.types.dash_ttml_configuration.serialize_json(
                value["ttml_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DashSubtitleConfiguration:
    out: DashSubtitleConfiguration = {}  # type: ignore[typeddict-item]
    if "TtmlConfiguration" in data:
        import capo_mediapackagev2.types.dash_ttml_configuration

        out["ttml_configuration"] = (
            capo_mediapackagev2.types.dash_ttml_configuration.deserialize_json(
                data["TtmlConfiguration"]
            )
        )
    return out
