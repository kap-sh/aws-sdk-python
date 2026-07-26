"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeDomainAutoTunesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.auto_tune_list
    import capo_opensearch.types.next_token


class DescribeDomainAutoTunesResponse(TypedDict, closed=True):
    auto_tunes: NotRequired["capo_opensearch.types.auto_tune_list.AutoTuneList"]
    """<p>The list of setting adjustments that Auto-Tune has made to the domain.</p>"""
    next_token: NotRequired["capo_opensearch.types.next_token.NextToken"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainAutoTunesResponse) -> dict:
    out: dict = {}
    if "auto_tunes" in value:
        import capo_opensearch.types.auto_tune_list

        out["AutoTunes"] = capo_opensearch.types.auto_tune_list.serialize_json(
            value["auto_tunes"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeDomainAutoTunesResponse:
    out: DescribeDomainAutoTunesResponse = {}  # type: ignore[typeddict-item]
    if "AutoTunes" in data:
        import capo_opensearch.types.auto_tune_list

        out["auto_tunes"] = capo_opensearch.types.auto_tune_list.deserialize_json(
            data["AutoTunes"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
