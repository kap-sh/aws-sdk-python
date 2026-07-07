"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListUserJourneysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.max_results
    import aws_sdk_resiliencehubv2.types.next_token


class ListUserJourneysRequest(TypedDict, closed=True):
    system_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    max_results: "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
    next_token: NotRequired["aws_sdk_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListUserJourneysRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListUserJourneysRequest:
    out: ListUserJourneysRequest = {}  # type: ignore[typeddict-item]
    return out
