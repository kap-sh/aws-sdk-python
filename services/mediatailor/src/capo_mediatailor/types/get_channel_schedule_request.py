"""Generated from Smithy shape ``com.amazonaws.mediatailor#GetChannelScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.max_results


class GetChannelScheduleRequest(TypedDict, closed=True):
    channel_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the channel associated with this Channel Schedule.</p>"""
    duration_minutes: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The duration in minutes of the channel schedule.</p>"""
    max_results: NotRequired["capo_mediatailor.types.max_results.MaxResults"]
    """<p>The maximum number of channel schedules that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> channel schedules, use the value of <code>NextToken</code> in the response to get the next page of results.</p>"""
    next_token: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>(Optional) If the playback configuration has more than <code>MaxResults</code> channel schedules, use <code>NextToken</code> to get the second and subsequent pages of results.</p> <p>For the first <code>GetChannelScheduleRequest</code> request, omit this value.</p> <p>For the second and subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request.</p> <p>If the previous response didn't include a <code>NextToken</code> element, there are no more channel schedules to get.</p>"""
    audience: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The single audience for GetChannelScheduleRequest.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelScheduleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetChannelScheduleRequest:
    out: GetChannelScheduleRequest = {}  # type: ignore[typeddict-item]
    return out
