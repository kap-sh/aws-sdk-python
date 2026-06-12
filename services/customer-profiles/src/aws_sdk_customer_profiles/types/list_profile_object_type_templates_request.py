"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListProfileObjectTypeTemplatesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.max_size100
    import aws_sdk_customer_profiles.types.token


class ListProfileObjectTypeTemplatesRequest(TypedDict):
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous ListObjectTypeTemplates API call.</p>"""
    max_results: NotRequired["aws_sdk_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of objects returned per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileObjectTypeTemplatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProfileObjectTypeTemplatesRequest:
    out: ListProfileObjectTypeTemplatesRequest = {}  # type: ignore[typeddict-item]
    return out
