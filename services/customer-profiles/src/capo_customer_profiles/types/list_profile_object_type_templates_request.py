"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListProfileObjectTypeTemplatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.max_size100
    import capo_customer_profiles.types.token


class ListProfileObjectTypeTemplatesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous ListObjectTypeTemplates API call.</p>"""
    max_results: NotRequired["capo_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of objects returned per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileObjectTypeTemplatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProfileObjectTypeTemplatesRequest:
    out: ListProfileObjectTypeTemplatesRequest = {}  # type: ignore[typeddict-item]
    return out
