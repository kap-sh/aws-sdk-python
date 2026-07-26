"""Generated from Smithy shape ``com.amazonaws.securityhub#GetFindingAggregatorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class GetFindingAggregatorRequest(TypedDict, closed=True):
    finding_aggregator_arn: "capo_securityhub.types.non_empty_string.NonEmptyString"
    """<p>The ARN of the finding aggregator to return details for. To obtain the ARN, use <code>ListFindingAggregators</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingAggregatorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFindingAggregatorRequest:
    out: GetFindingAggregatorRequest = {}  # type: ignore[typeddict-item]
    return out
