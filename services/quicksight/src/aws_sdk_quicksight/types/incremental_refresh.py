"""Generated from Smithy shape ``com.amazonaws.quicksight#IncrementalRefresh``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.lookback_window


class IncrementalRefresh(TypedDict):
    lookback_window: "aws_sdk_quicksight.types.lookback_window.LookbackWindow"
    """<p>The lookback window setup for an incremental refresh configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncrementalRefresh) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.lookback_window

    out["LookbackWindow"] = aws_sdk_quicksight.types.lookback_window.serialize_json(
        value["lookback_window"]
    )
    return out


def deserialize_json(data: dict) -> IncrementalRefresh:
    out: IncrementalRefresh = {}  # type: ignore[typeddict-item]
    if "LookbackWindow" in data:
        import aws_sdk_quicksight.types.lookback_window

        out["lookback_window"] = (
            aws_sdk_quicksight.types.lookback_window.deserialize_json(
                data["LookbackWindow"]
            )
        )
    else:
        raise DeserializationError("IncrementalRefresh.lookback_window required")
    return out
