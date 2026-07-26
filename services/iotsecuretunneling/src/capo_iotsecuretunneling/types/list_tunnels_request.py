"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#ListTunnelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsecuretunneling.types.max_results
    import capo_iotsecuretunneling.types.next_token
    import capo_iotsecuretunneling.types.thing_name


class ListTunnelsRequest(TypedDict, closed=True):
    thing_name: NotRequired["capo_iotsecuretunneling.types.thing_name.ThingName"]
    """<p>The name of the IoT thing associated with the destination device.</p>"""
    max_results: NotRequired["capo_iotsecuretunneling.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at once.</p>"""
    next_token: NotRequired["capo_iotsecuretunneling.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the nextToken value from a previous response; otherwise null to receive the first set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTunnelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTunnelsRequest:
    out: ListTunnelsRequest = {}  # type: ignore[typeddict-item]
    return out
