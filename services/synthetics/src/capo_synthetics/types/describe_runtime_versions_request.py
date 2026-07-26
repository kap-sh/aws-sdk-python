"""Generated from Smithy shape ``com.amazonaws.synthetics#DescribeRuntimeVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.max_size100
    import capo_synthetics.types.token


class DescribeRuntimeVersionsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_synthetics.types.token.Token"]
    """<p>A token that indicates that there is more data available. You can use this token in a subsequent <code>DescribeRuntimeVersions</code> operation to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_synthetics.types.max_size100.MaxSize100"]
    """<p>Specify this parameter to limit how many runs are returned each time you use the <code>DescribeRuntimeVersions</code> operation. If you omit this parameter, the default of 100 is used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRuntimeVersionsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> DescribeRuntimeVersionsRequest:
    out: DescribeRuntimeVersionsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
