"""Generated from Smithy shape ``com.amazonaws.quicksight#BinCountOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.bin_count_value


class BinCountOptions(TypedDict, closed=True):
    value: NotRequired["aws_sdk_quicksight.types.bin_count_value.BinCountValue"]
    """<p>The options that determine the bin count value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BinCountOptions) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> BinCountOptions:
    out: BinCountOptions = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
