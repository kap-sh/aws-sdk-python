"""Generated from Smithy shape ``com.amazonaws.artifact#ListCustomerAgreementsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_artifact.types.max_results_attribute
    import aws_sdk_artifact.types.next_token_attribute


class ListCustomerAgreementsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "aws_sdk_artifact.types.max_results_attribute.MaxResultsAttribute"
    ]
    """<p>Maximum number of resources to return in the paginated response.</p>"""
    next_token: NotRequired[
        "aws_sdk_artifact.types.next_token_attribute.NextTokenAttribute"
    ]
    """<p>Pagination token to request the next page of resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomerAgreementsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCustomerAgreementsRequest:
    out: ListCustomerAgreementsRequest = {}  # type: ignore[typeddict-item]
    return out
