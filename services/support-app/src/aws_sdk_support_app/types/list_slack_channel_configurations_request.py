"""Generated from Smithy shape ``com.amazonaws.supportapp#ListSlackChannelConfigurationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_support_app.types.pagination_token


class ListSlackChannelConfigurationsRequest(TypedDict):
    next_token: NotRequired[
        "aws_sdk_support_app.types.pagination_token.paginationToken"
    ]
    """<p>If the results of a search are large, the API only returns a portion of the results and includes a <code>nextToken</code> pagination token in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When the API returns the last set of results, the response doesn't include a pagination token value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSlackChannelConfigurationsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSlackChannelConfigurationsRequest:
    out: ListSlackChannelConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
