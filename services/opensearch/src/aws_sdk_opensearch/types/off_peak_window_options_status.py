"""Generated from Smithy shape ``com.amazonaws.opensearch#OffPeakWindowOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.off_peak_window_options
    import aws_sdk_opensearch.types.option_status


class OffPeakWindowOptionsStatus(TypedDict, closed=True):
    options: NotRequired[
        "aws_sdk_opensearch.types.off_peak_window_options.OffPeakWindowOptions"
    ]
    """<p>The domain's off-peak window configuration.</p>"""
    status: NotRequired["aws_sdk_opensearch.types.option_status.OptionStatus"]
    """<p>The current status of off-peak window options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OffPeakWindowOptionsStatus) -> dict:
    out: dict = {}
    if "options" in value:
        import aws_sdk_opensearch.types.off_peak_window_options

        out["Options"] = (
            aws_sdk_opensearch.types.off_peak_window_options.serialize_json(
                value["options"]
            )
        )
    if "status" in value:
        import aws_sdk_opensearch.types.option_status

        out["Status"] = aws_sdk_opensearch.types.option_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> OffPeakWindowOptionsStatus:
    out: OffPeakWindowOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import aws_sdk_opensearch.types.off_peak_window_options

        out["options"] = (
            aws_sdk_opensearch.types.off_peak_window_options.deserialize_json(
                data["Options"]
            )
        )
    if "Status" in data:
        import aws_sdk_opensearch.types.option_status

        out["status"] = aws_sdk_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    return out
