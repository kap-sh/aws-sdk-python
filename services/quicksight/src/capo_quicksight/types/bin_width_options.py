"""Generated from Smithy shape ``com.amazonaws.quicksight#BinWidthOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.bin_count_limit
    import capo_quicksight.types.bin_width_value


class BinWidthOptions(TypedDict, closed=True):
    value: NotRequired["capo_quicksight.types.bin_width_value.BinWidthValue"]
    """<p>The options that determine the bin width value.</p>"""
    bin_count_limit: NotRequired["capo_quicksight.types.bin_count_limit.BinCountLimit"]
    """<p>The options that determine the bin count limit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BinWidthOptions) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "bin_count_limit" in value:
        out["BinCountLimit"] = value["bin_count_limit"]
    return out


def deserialize_json(data: dict) -> BinWidthOptions:
    out: BinWidthOptions = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    if "BinCountLimit" in data:
        out["bin_count_limit"] = data["BinCountLimit"]
    return out
