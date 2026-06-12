"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#Recommendation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.matches
    import aws_sdk_codeguruprofiler.types.pattern
    import aws_sdk_codeguruprofiler.types.timestamp


class Recommendation(TypedDict):
    all_matches_count: "int"
    """<p>How many different places in the profile graph triggered a match.</p>"""
    all_matches_sum: "float"
    """<p>How much of the total sample count is potentially affected.</p>"""
    pattern: "aws_sdk_codeguruprofiler.types.pattern.Pattern"
    """<p>The pattern that analysis recognized in the profile to make this recommendation.</p>"""
    top_matches: "aws_sdk_codeguruprofiler.types.matches.Matches"
    """<p>List of the matches with most impact. </p>"""
    start_time: "aws_sdk_codeguruprofiler.types.timestamp.Timestamp"
    """<p>The start time of the profile that was used by this analysis. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.</p>"""
    end_time: "aws_sdk_codeguruprofiler.types.timestamp.Timestamp"
    """<p>End time of the profile that was used by this analysis. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Recommendation) -> dict:
    out: dict = {}
    out["allMatchesCount"] = value["all_matches_count"]
    out["allMatchesSum"] = value["all_matches_sum"]
    import aws_sdk_codeguruprofiler.types.pattern

    out["pattern"] = aws_sdk_codeguruprofiler.types.pattern.serialize_json(
        value["pattern"]
    )
    import aws_sdk_codeguruprofiler.types.matches

    out["topMatches"] = aws_sdk_codeguruprofiler.types.matches.serialize_json(
        value["top_matches"]
    )
    import aws_sdk_codeguruprofiler.types.timestamp

    out["startTime"] = aws_sdk_codeguruprofiler.types.timestamp.serialize_json(
        value["start_time"]
    )
    import aws_sdk_codeguruprofiler.types.timestamp

    out["endTime"] = aws_sdk_codeguruprofiler.types.timestamp.serialize_json(
        value["end_time"]
    )
    return out


def deserialize_json(data: dict) -> Recommendation:
    out: Recommendation = {}  # type: ignore[typeddict-item]
    if "allMatchesCount" in data:
        out["all_matches_count"] = data["allMatchesCount"]
    else:
        raise DeserializationError("Recommendation.all_matches_count required")
    if "allMatchesSum" in data:
        out["all_matches_sum"] = data["allMatchesSum"]
    else:
        raise DeserializationError("Recommendation.all_matches_sum required")
    if "pattern" in data:
        import aws_sdk_codeguruprofiler.types.pattern

        out["pattern"] = aws_sdk_codeguruprofiler.types.pattern.deserialize_json(
            data["pattern"]
        )
    else:
        raise DeserializationError("Recommendation.pattern required")
    if "topMatches" in data:
        import aws_sdk_codeguruprofiler.types.matches

        out["top_matches"] = aws_sdk_codeguruprofiler.types.matches.deserialize_json(
            data["topMatches"]
        )
    else:
        raise DeserializationError("Recommendation.top_matches required")
    if "startTime" in data:
        import aws_sdk_codeguruprofiler.types.timestamp

        out["start_time"] = aws_sdk_codeguruprofiler.types.timestamp.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("Recommendation.start_time required")
    if "endTime" in data:
        import aws_sdk_codeguruprofiler.types.timestamp

        out["end_time"] = aws_sdk_codeguruprofiler.types.timestamp.deserialize_json(
            data["endTime"]
        )
    else:
        raise DeserializationError("Recommendation.end_time required")
    return out
