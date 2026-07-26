"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListReservationOfferingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.pagination_token


class ListReservationOfferingsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_redshift_serverless.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListReservationOfferingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ListReservationOfferingsRequest:
    out: ListReservationOfferingsRequest = {}  # type: ignore[typeddict-item]
    return out
