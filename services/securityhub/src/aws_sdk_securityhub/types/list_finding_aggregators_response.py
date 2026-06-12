"""Generated from Smithy shape ``com.amazonaws.securityhub#ListFindingAggregatorsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.finding_aggregator_list
    import aws_sdk_securityhub.types.next_token


class ListFindingAggregatorsResponse(TypedDict):
    finding_aggregators: NotRequired[
        "aws_sdk_securityhub.types.finding_aggregator_list.FindingAggregatorList"
    ]
    """<p>The list of finding aggregators. This operation currently only returns a single result.</p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>If there are more results, this is the token to provide in the next call to <code>ListFindingAggregators</code>.</p> <p>This operation currently only returns a single result. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingAggregatorsResponse) -> dict:
    out: dict = {}
    if "finding_aggregators" in value:
        import aws_sdk_securityhub.types.finding_aggregator_list

        out["FindingAggregators"] = (
            aws_sdk_securityhub.types.finding_aggregator_list.serialize_json(
                value["finding_aggregators"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFindingAggregatorsResponse:
    out: ListFindingAggregatorsResponse = {}  # type: ignore[typeddict-item]
    if "FindingAggregators" in data:
        import aws_sdk_securityhub.types.finding_aggregator_list

        out["finding_aggregators"] = (
            aws_sdk_securityhub.types.finding_aggregator_list.deserialize_json(
                data["FindingAggregators"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
