"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#GetRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.anomalies
    import aws_sdk_codeguruprofiler.types.profiling_group_name
    import aws_sdk_codeguruprofiler.types.recommendations
    import aws_sdk_codeguruprofiler.types.timestamp


class GetRecommendationsResponse(TypedDict, closed=True):
    profiling_group_name: (
        "aws_sdk_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    )
    """<p>The name of the profiling group the analysis data is about.</p>"""
    profile_start_time: "aws_sdk_codeguruprofiler.types.timestamp.Timestamp"
    """<p> The start time of the profile the analysis data is about. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    profile_end_time: "aws_sdk_codeguruprofiler.types.timestamp.Timestamp"
    """<p> The end time of the profile the analysis data is about. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    recommendations: "aws_sdk_codeguruprofiler.types.recommendations.Recommendations"
    """<p>The list of recommendations that the analysis found for this profile.</p>"""
    anomalies: "aws_sdk_codeguruprofiler.types.anomalies.Anomalies"
    """<p> The list of anomalies that the analysis has found for this profile. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendationsResponse) -> dict:
    out: dict = {}
    out["profilingGroupName"] = value["profiling_group_name"]
    import aws_sdk_codeguruprofiler.types.timestamp

    out["profileStartTime"] = aws_sdk_codeguruprofiler.types.timestamp.serialize_json(
        value["profile_start_time"]
    )
    import aws_sdk_codeguruprofiler.types.timestamp

    out["profileEndTime"] = aws_sdk_codeguruprofiler.types.timestamp.serialize_json(
        value["profile_end_time"]
    )
    import aws_sdk_codeguruprofiler.types.recommendations

    out["recommendations"] = (
        aws_sdk_codeguruprofiler.types.recommendations.serialize_json(
            value["recommendations"]
        )
    )
    import aws_sdk_codeguruprofiler.types.anomalies

    out["anomalies"] = aws_sdk_codeguruprofiler.types.anomalies.serialize_json(
        value["anomalies"]
    )
    return out


def deserialize_json(data: dict) -> GetRecommendationsResponse:
    out: GetRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "profilingGroupName" in data:
        out["profiling_group_name"] = data["profilingGroupName"]
    else:
        raise DeserializationError(
            "GetRecommendationsResponse.profiling_group_name required"
        )
    if "profileStartTime" in data:
        import aws_sdk_codeguruprofiler.types.timestamp

        out["profile_start_time"] = (
            aws_sdk_codeguruprofiler.types.timestamp.deserialize_json(
                data["profileStartTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetRecommendationsResponse.profile_start_time required"
        )
    if "profileEndTime" in data:
        import aws_sdk_codeguruprofiler.types.timestamp

        out["profile_end_time"] = (
            aws_sdk_codeguruprofiler.types.timestamp.deserialize_json(
                data["profileEndTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetRecommendationsResponse.profile_end_time required"
        )
    if "recommendations" in data:
        import aws_sdk_codeguruprofiler.types.recommendations

        out["recommendations"] = (
            aws_sdk_codeguruprofiler.types.recommendations.deserialize_json(
                data["recommendations"]
            )
        )
    else:
        raise DeserializationError(
            "GetRecommendationsResponse.recommendations required"
        )
    if "anomalies" in data:
        import aws_sdk_codeguruprofiler.types.anomalies

        out["anomalies"] = aws_sdk_codeguruprofiler.types.anomalies.deserialize_json(
            data["anomalies"]
        )
    else:
        raise DeserializationError("GetRecommendationsResponse.anomalies required")
    return out
