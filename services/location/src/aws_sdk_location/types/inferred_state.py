"""Generated from Smithy shape ``com.amazonaws.location#InferredState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.position
    import aws_sdk_location.types.positional_accuracy


class InferredState(TypedDict):
    position: NotRequired["aws_sdk_location.types.position.Position"]
    """<p>The device position inferred by the provided position, IP address, cellular signals, and Wi-Fi- access points.</p>"""
    accuracy: NotRequired[
        "aws_sdk_location.types.positional_accuracy.PositionalAccuracy"
    ]
    """<p>The level of certainty of the inferred position.</p>"""
    deviation_distance: NotRequired["float"]
    """<p>The distance between the inferred position and the device's self-reported position.</p>"""
    proxy_detected: "bool"
    """<p>Indicates if a proxy was used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InferredState) -> dict:
    out: dict = {}
    if "position" in value:
        import aws_sdk_location.types.position

        out["Position"] = aws_sdk_location.types.position.serialize_json(
            value["position"]
        )
    if "accuracy" in value:
        import aws_sdk_location.types.positional_accuracy

        out["Accuracy"] = aws_sdk_location.types.positional_accuracy.serialize_json(
            value["accuracy"]
        )
    if "deviation_distance" in value:
        out["DeviationDistance"] = value["deviation_distance"]
    out["ProxyDetected"] = value["proxy_detected"]
    return out


def deserialize_json(data: dict) -> InferredState:
    out: InferredState = {}  # type: ignore[typeddict-item]
    if "Position" in data:
        import aws_sdk_location.types.position

        out["position"] = aws_sdk_location.types.position.deserialize_json(
            data["Position"]
        )
    if "Accuracy" in data:
        import aws_sdk_location.types.positional_accuracy

        out["accuracy"] = aws_sdk_location.types.positional_accuracy.deserialize_json(
            data["Accuracy"]
        )
    if "DeviationDistance" in data:
        out["deviation_distance"] = data["DeviationDistance"]
    if "ProxyDetected" in data:
        out["proxy_detected"] = data["ProxyDetected"]
    else:
        raise DeserializationError("InferredState.proxy_detected required")
    return out
