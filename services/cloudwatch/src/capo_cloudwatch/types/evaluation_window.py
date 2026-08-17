"""Generated from Smithy shape ``com.amazonaws.cloudwatch#EvaluationWindow``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cloudwatch._protocol.xml import Element
from capo_cloudwatch.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_cloudwatch.types.sliding_window
    import capo_cloudwatch.types.wall_clock_window


class _EvaluationWindow_WallClockWindow(TypedDict, closed=True):
    WallClockWindow: "capo_cloudwatch.types.wall_clock_window.WallClockWindow"


class _EvaluationWindow_SlidingWindow(TypedDict, closed=True):
    SlidingWindow: "capo_cloudwatch.types.sliding_window.SlidingWindow"


EvaluationWindow: TypeAlias = (
    _EvaluationWindow_WallClockWindow | _EvaluationWindow_SlidingWindow
)


# --- awsQuery ser/de ---
def serialize_query(
    value: EvaluationWindow, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "WallClockWindow" in value:
        import capo_cloudwatch.types.wall_clock_window

        capo_cloudwatch.types.wall_clock_window.serialize_query(
            value["WallClockWindow"], pairs, f"{prefix}.WallClockWindow"
        )
    elif "SlidingWindow" in value:
        import capo_cloudwatch.types.sliding_window

        capo_cloudwatch.types.sliding_window.serialize_query(
            value["SlidingWindow"], pairs, f"{prefix}.SlidingWindow"
        )
    else:
        raise SerializationError("EvaluationWindow: no variant present")


def deserialize_query(el: Element) -> EvaluationWindow:
    for child in el:
        if child.tag == "WallClockWindow":
            import capo_cloudwatch.types.wall_clock_window

            return {
                "WallClockWindow": capo_cloudwatch.types.wall_clock_window.deserialize_query(
                    child
                )
            }
        elif child.tag == "SlidingWindow":
            import capo_cloudwatch.types.sliding_window

            return {
                "SlidingWindow": capo_cloudwatch.types.sliding_window.deserialize_query(
                    child
                )
            }
    raise DeserializationError("EvaluationWindow: no recognized variant element")


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EvaluationWindow) -> dict:
    if "WallClockWindow" in value:
        import capo_cloudwatch.types.wall_clock_window

        return {
            "WallClockWindow": capo_cloudwatch.types.wall_clock_window.serialize_aws_json_1_0(
                value["WallClockWindow"]
            )
        }
    elif "SlidingWindow" in value:
        import capo_cloudwatch.types.sliding_window

        return {
            "SlidingWindow": capo_cloudwatch.types.sliding_window.serialize_aws_json_1_0(
                value["SlidingWindow"]
            )
        }
    else:
        raise SerializationError("EvaluationWindow: no variant present")


def deserialize_aws_json_1_0(data: dict) -> EvaluationWindow:
    if data.get("WallClockWindow") is not None:
        import capo_cloudwatch.types.wall_clock_window

        return {
            "WallClockWindow": capo_cloudwatch.types.wall_clock_window.deserialize_aws_json_1_0(
                data["WallClockWindow"]
            )
        }
    elif data.get("SlidingWindow") is not None:
        import capo_cloudwatch.types.sliding_window

        return {
            "SlidingWindow": capo_cloudwatch.types.sliding_window.deserialize_aws_json_1_0(
                data["SlidingWindow"]
            )
        }
    else:
        raise DeserializationError("EvaluationWindow: no recognized variant key")
