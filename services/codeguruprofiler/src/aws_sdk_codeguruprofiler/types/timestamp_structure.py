"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#TimestampStructure``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.timestamp


class TimestampStructure(TypedDict):
    value: "aws_sdk_codeguruprofiler.types.timestamp.Timestamp"
    """<p> A <code>Timestamp</code>. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimestampStructure) -> dict:
    out: dict = {}
    import aws_sdk_codeguruprofiler.types.timestamp

    out["value"] = aws_sdk_codeguruprofiler.types.timestamp.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> TimestampStructure:
    out: TimestampStructure = {}  # type: ignore[typeddict-item]
    if "value" in data:
        import aws_sdk_codeguruprofiler.types.timestamp

        out["value"] = aws_sdk_codeguruprofiler.types.timestamp.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("TimestampStructure.value required")
    return out
