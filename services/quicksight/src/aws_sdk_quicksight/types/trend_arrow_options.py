"""Generated from Smithy shape ``com.amazonaws.quicksight#TrendArrowOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.visibility


class TrendArrowOptions(TypedDict):
    visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the trend arrows.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrendArrowOptions) -> dict:
    out: dict = {}
    if "visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["Visibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    return out


def deserialize_json(data: dict) -> TrendArrowOptions:
    out: TrendArrowOptions = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    return out
