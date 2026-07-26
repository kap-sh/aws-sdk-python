"""Generated from Smithy shape ``com.amazonaws.quicksight#HistogramBinOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.bin_count_options
    import capo_quicksight.types.bin_width_options
    import capo_quicksight.types.double
    import capo_quicksight.types.histogram_bin_type


class HistogramBinOptions(TypedDict, closed=True):
    selected_bin_type: NotRequired[
        "capo_quicksight.types.histogram_bin_type.HistogramBinType"
    ]
    """<p>The options that determine the selected bin type.</p>"""
    bin_count: NotRequired["capo_quicksight.types.bin_count_options.BinCountOptions"]
    """<p>The options that determine the bin count of a histogram.</p>"""
    bin_width: NotRequired["capo_quicksight.types.bin_width_options.BinWidthOptions"]
    """<p>The options that determine the bin width of a histogram.</p>"""
    start_value: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The options that determine the bin start value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HistogramBinOptions) -> dict:
    out: dict = {}
    if "selected_bin_type" in value:
        import capo_quicksight.types.histogram_bin_type

        out["SelectedBinType"] = (
            capo_quicksight.types.histogram_bin_type.serialize_json(
                value["selected_bin_type"]
            )
        )
    if "bin_count" in value:
        import capo_quicksight.types.bin_count_options

        out["BinCount"] = capo_quicksight.types.bin_count_options.serialize_json(
            value["bin_count"]
        )
    if "bin_width" in value:
        import capo_quicksight.types.bin_width_options

        out["BinWidth"] = capo_quicksight.types.bin_width_options.serialize_json(
            value["bin_width"]
        )
    if "start_value" in value:
        out["StartValue"] = value["start_value"]
    return out


def deserialize_json(data: dict) -> HistogramBinOptions:
    out: HistogramBinOptions = {}  # type: ignore[typeddict-item]
    if "SelectedBinType" in data:
        import capo_quicksight.types.histogram_bin_type

        out["selected_bin_type"] = (
            capo_quicksight.types.histogram_bin_type.deserialize_json(
                data["SelectedBinType"]
            )
        )
    if "BinCount" in data:
        import capo_quicksight.types.bin_count_options

        out["bin_count"] = capo_quicksight.types.bin_count_options.deserialize_json(
            data["BinCount"]
        )
    if "BinWidth" in data:
        import capo_quicksight.types.bin_width_options

        out["bin_width"] = capo_quicksight.types.bin_width_options.deserialize_json(
            data["BinWidth"]
        )
    if "StartValue" in data:
        out["start_value"] = data["StartValue"]
    return out
