"""Generated from Smithy shape ``com.amazonaws.iotsitewise#MetricWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.tumbling_window


class MetricWindow(TypedDict, closed=True):
    tumbling: NotRequired["aws_sdk_iotsitewise.types.tumbling_window.TumblingWindow"]
    """<p>The tumbling time interval window.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricWindow) -> dict:
    out: dict = {}
    if "tumbling" in value:
        import aws_sdk_iotsitewise.types.tumbling_window

        out["tumbling"] = aws_sdk_iotsitewise.types.tumbling_window.serialize_json(
            value["tumbling"]
        )
    return out


def deserialize_json(data: dict) -> MetricWindow:
    out: MetricWindow = {}  # type: ignore[typeddict-item]
    if "tumbling" in data:
        import aws_sdk_iotsitewise.types.tumbling_window

        out["tumbling"] = aws_sdk_iotsitewise.types.tumbling_window.deserialize_json(
            data["tumbling"]
        )
    return out
