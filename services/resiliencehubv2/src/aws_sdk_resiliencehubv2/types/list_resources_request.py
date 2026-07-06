"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.aws_region
    import aws_sdk_resiliencehubv2.types.entity_id
    import aws_sdk_resiliencehubv2.types.max_results
    import aws_sdk_resiliencehubv2.types.next_token


class ListResourcesRequest(TypedDict, closed=True):
    service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    service_function_id: NotRequired["aws_sdk_resiliencehubv2.types.entity_id.EntityId"]
    """<p>Filter resources by service function identifier.</p>"""
    aws_region: NotRequired["aws_sdk_resiliencehubv2.types.aws_region.AwsRegion"]
    """<p>Filter resources by AWS Region.</p>"""
    max_results: "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
    next_token: NotRequired["aws_sdk_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListResourcesRequest:
    out: ListResourcesRequest = {}  # type: ignore[typeddict-item]
    return out
