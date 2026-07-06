"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetRecommenderConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class GetRecommenderConfigurationsRequest(TypedDict, closed=True):
    page_size: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>"""
    token: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The NextToken string that specifies which page of results to return in a paginated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommenderConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRecommenderConfigurationsRequest:
    out: GetRecommenderConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
