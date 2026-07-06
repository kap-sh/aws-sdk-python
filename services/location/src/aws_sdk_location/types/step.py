"""Generated from Smithy shape ``com.amazonaws.location#Step``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.position
    import aws_sdk_location.types.sensitive_double


class Step(TypedDict, closed=True):
    start_position: "aws_sdk_location.types.position.Position"
    """<p>The starting position of a step. If the position is the first step in the leg, this position is the same as the start position of the leg.</p>"""
    end_position: "aws_sdk_location.types.position.Position"
    """<p>The end position of a step. If the position the last step in the leg, this position is the same as the end position of the leg.</p>"""
    distance: "aws_sdk_location.types.sensitive_double.SensitiveDouble"
    """<p>The travel distance between the step's <code>StartPosition</code> and <code>EndPosition</code>.</p>"""
    duration_seconds: "aws_sdk_location.types.sensitive_double.SensitiveDouble"
    """<p>The estimated travel time, in seconds, from the step's <code>StartPosition</code> to the <code>EndPosition</code>. . The travel mode and departure time that you specify in the request determines the calculated time.</p>"""
    geometry_offset: NotRequired["int"]
    """<p>Represents the start position, or index, in a sequence of steps within the leg's line string geometry. For example, the index of the first step in a leg geometry is <code>0</code>. </p> <p>Included in the response for queries that set <code>IncludeLegGeometry</code> to <code>True</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Step) -> dict:
    out: dict = {}
    import aws_sdk_location.types.position

    out["StartPosition"] = aws_sdk_location.types.position.serialize_json(
        value["start_position"]
    )
    import aws_sdk_location.types.position

    out["EndPosition"] = aws_sdk_location.types.position.serialize_json(
        value["end_position"]
    )
    out["Distance"] = value["distance"]
    out["DurationSeconds"] = value["duration_seconds"]
    if "geometry_offset" in value:
        out["GeometryOffset"] = value["geometry_offset"]
    return out


def deserialize_json(data: dict) -> Step:
    out: Step = {}  # type: ignore[typeddict-item]
    if "StartPosition" in data:
        import aws_sdk_location.types.position

        out["start_position"] = aws_sdk_location.types.position.deserialize_json(
            data["StartPosition"]
        )
    else:
        raise DeserializationError("Step.start_position required")
    if "EndPosition" in data:
        import aws_sdk_location.types.position

        out["end_position"] = aws_sdk_location.types.position.deserialize_json(
            data["EndPosition"]
        )
    else:
        raise DeserializationError("Step.end_position required")
    if "Distance" in data:
        out["distance"] = data["Distance"]
    else:
        raise DeserializationError("Step.distance required")
    if "DurationSeconds" in data:
        out["duration_seconds"] = data["DurationSeconds"]
    else:
        raise DeserializationError("Step.duration_seconds required")
    if "GeometryOffset" in data:
        out["geometry_offset"] = data["GeometryOffset"]
    return out
