"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListSystemsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.max_results
    import aws_sdk_resiliencehubv2.types.next_token
    import aws_sdk_resiliencehubv2.types.ou_id


class ListSystemsRequest(TypedDict, closed=True):
    ou_id: NotRequired["aws_sdk_resiliencehubv2.types.ou_id.OuId"]
    """<p>Filter systems by organizational unit (OU) identifier.</p>"""
    max_results: "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
    next_token: NotRequired["aws_sdk_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListSystemsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSystemsRequest:
    out: ListSystemsRequest = {}  # type: ignore[typeddict-item]
    return out
