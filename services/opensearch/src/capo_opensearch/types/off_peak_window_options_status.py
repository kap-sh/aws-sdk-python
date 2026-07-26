"""Generated from Smithy shape ``com.amazonaws.opensearch#OffPeakWindowOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.off_peak_window_options
    import capo_opensearch.types.option_status


class OffPeakWindowOptionsStatus(TypedDict, closed=True):
    options: NotRequired[
        "capo_opensearch.types.off_peak_window_options.OffPeakWindowOptions"
    ]
    """<p>The domain's off-peak window configuration.</p>"""
    status: NotRequired["capo_opensearch.types.option_status.OptionStatus"]
    """<p>The current status of off-peak window options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OffPeakWindowOptionsStatus) -> dict:
    out: dict = {}
    if "options" in value:
        import capo_opensearch.types.off_peak_window_options

        out["Options"] = capo_opensearch.types.off_peak_window_options.serialize_json(
            value["options"]
        )
    if "status" in value:
        import capo_opensearch.types.option_status

        out["Status"] = capo_opensearch.types.option_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> OffPeakWindowOptionsStatus:
    out: OffPeakWindowOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import capo_opensearch.types.off_peak_window_options

        out["options"] = capo_opensearch.types.off_peak_window_options.deserialize_json(
            data["Options"]
        )
    if "Status" in data:
        import capo_opensearch.types.option_status

        out["status"] = capo_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    return out
