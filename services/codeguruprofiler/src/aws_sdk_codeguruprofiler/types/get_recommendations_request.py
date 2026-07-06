"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#GetRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.locale
    import aws_sdk_codeguruprofiler.types.profiling_group_name
    import aws_sdk_codeguruprofiler.types.timestamp


class GetRecommendationsRequest(TypedDict, closed=True):
    profiling_group_name: (
        "aws_sdk_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    )
    """<p> The name of the profiling group to get analysis data about. </p>"""
    start_time: "aws_sdk_codeguruprofiler.types.timestamp.Timestamp"
    """<p> The end time of the profile to get analysis data about. You must specify <code>startTime</code> and <code>endTime</code>. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    end_time: "aws_sdk_codeguruprofiler.types.timestamp.Timestamp"
    """<p> The start time of the profile to get analysis data about. You must specify <code>startTime</code> and <code>endTime</code>. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    locale: NotRequired["aws_sdk_codeguruprofiler.types.locale.Locale"]
    """<p> The language used to provide analysis. Specify using a string that is one of the following <code>BCP 47</code> language codes. </p> <ul> <li> <p> <code>de-DE</code> - German, Germany </p> </li> <li> <p> <code>en-GB</code> - English, United Kingdom </p> </li> <li> <p> <code>en-US</code> - English, United States </p> </li> <li> <p> <code>es-ES</code> - Spanish, Spain </p> </li> <li> <p> <code>fr-FR</code> - French, France </p> </li> <li> <p> <code>it-IT</code> - Italian, Italy </p> </li> <li> <p> <code>ja-JP</code> - Japanese, Japan </p> </li> <li> <p> <code>ko-KR</code> - Korean, Republic of Korea </p> </li> <li> <p> <code>pt-BR</code> - Portugese, Brazil </p> </li> <li> <p> <code>zh-CN</code> - Chinese, China </p> </li> <li> <p> <code>zh-TW</code> - Chinese, Taiwan </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRecommendationsRequest:
    out: GetRecommendationsRequest = {}  # type: ignore[typeddict-item]
    return out
