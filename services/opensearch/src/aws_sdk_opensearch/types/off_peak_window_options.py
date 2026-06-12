"""Generated from Smithy shape ``com.amazonaws.opensearch#OffPeakWindowOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.off_peak_window


class OffPeakWindowOptions(TypedDict):
    enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Whether to enable an off-peak window.</p> <p>This option is only available when modifying a domain created prior to February 16, 2023, not when creating a new domain. All domains created after this date have the off-peak window enabled by default. You can't disable the off-peak window after it's enabled for a domain.</p>"""
    off_peak_window: NotRequired[
        "aws_sdk_opensearch.types.off_peak_window.OffPeakWindow"
    ]
    """<p>Off-peak window settings for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OffPeakWindowOptions) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "off_peak_window" in value:
        import aws_sdk_opensearch.types.off_peak_window

        out["OffPeakWindow"] = aws_sdk_opensearch.types.off_peak_window.serialize_json(
            value["off_peak_window"]
        )
    return out


def deserialize_json(data: dict) -> OffPeakWindowOptions:
    out: OffPeakWindowOptions = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "OffPeakWindow" in data:
        import aws_sdk_opensearch.types.off_peak_window

        out["off_peak_window"] = (
            aws_sdk_opensearch.types.off_peak_window.deserialize_json(
                data["OffPeakWindow"]
            )
        )
    return out
