"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#ListPresetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.ascending
    import capo_elastic_transcoder.types.id


class ListPresetsRequest(TypedDict, closed=True):
    ascending: NotRequired["capo_elastic_transcoder.types.ascending.Ascending"]
    """<p>To list presets in chronological order by the date and time that they were created, enter <code>true</code>. To list presets in reverse chronological order, enter <code>false</code>.</p>"""
    page_token: NotRequired["capo_elastic_transcoder.types.id.Id"]
    """<p>When Elastic Transcoder returns more than one page of results, use <code>pageToken</code> in subsequent <code>GET</code> requests to get each successive page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPresetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPresetsRequest:
    out: ListPresetsRequest = {}  # type: ignore[typeddict-item]
    return out
