"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ProfileTime``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.timestamp


class ProfileTime(TypedDict, closed=True):
    start: NotRequired["aws_sdk_codeguruprofiler.types.timestamp.Timestamp"]
    """<p>The start time of a profile. It is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileTime) -> dict:
    out: dict = {}
    if "start" in value:
        import aws_sdk_codeguruprofiler.types.timestamp

        out["start"] = aws_sdk_codeguruprofiler.types.timestamp.serialize_json(
            value["start"]
        )
    return out


def deserialize_json(data: dict) -> ProfileTime:
    out: ProfileTime = {}  # type: ignore[typeddict-item]
    if "start" in data:
        import aws_sdk_codeguruprofiler.types.timestamp

        out["start"] = aws_sdk_codeguruprofiler.types.timestamp.deserialize_json(
            data["start"]
        )
    return out
