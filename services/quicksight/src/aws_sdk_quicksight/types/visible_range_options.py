"""Generated from Smithy shape ``com.amazonaws.quicksight#VisibleRangeOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.percent_visible_range


class VisibleRangeOptions(TypedDict, closed=True):
    percent_range: NotRequired[
        "aws_sdk_quicksight.types.percent_visible_range.PercentVisibleRange"
    ]
    """<p>The percent range in the visible range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisibleRangeOptions) -> dict:
    out: dict = {}
    if "percent_range" in value:
        import aws_sdk_quicksight.types.percent_visible_range

        out["PercentRange"] = (
            aws_sdk_quicksight.types.percent_visible_range.serialize_json(
                value["percent_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> VisibleRangeOptions:
    out: VisibleRangeOptions = {}  # type: ignore[typeddict-item]
    if "PercentRange" in data:
        import aws_sdk_quicksight.types.percent_visible_range

        out["percent_range"] = (
            aws_sdk_quicksight.types.percent_visible_range.deserialize_json(
                data["PercentRange"]
            )
        )
    return out
