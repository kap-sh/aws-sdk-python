"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListInputSourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.input_source_type
    import aws_sdk_resiliencehubv2.types.max_results
    import aws_sdk_resiliencehubv2.types.next_token


class ListInputSourcesRequest(TypedDict, closed=True):
    service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    type: NotRequired["aws_sdk_resiliencehubv2.types.input_source_type.InputSourceType"]
    """<p>Filter input sources by type.</p>"""
    max_results: "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
    next_token: NotRequired["aws_sdk_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListInputSourcesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListInputSourcesRequest:
    out: ListInputSourcesRequest = {}  # type: ignore[typeddict-item]
    return out
