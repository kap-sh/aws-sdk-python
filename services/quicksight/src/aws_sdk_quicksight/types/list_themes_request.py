"""Generated from Smithy shape ``com.amazonaws.quicksight#ListThemesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.max_results
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.theme_type


class ListThemesRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the themes that you're listing.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    max_results: NotRequired["aws_sdk_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned per request.</p>"""
    type: NotRequired["aws_sdk_quicksight.types.theme_type.ThemeType"]
    """<p>The type of themes that you want to list. Valid options include the following:</p> <ul> <li> <p> <code>ALL (default)</code>- Display all existing themes.</p> </li> <li> <p> <code>CUSTOM</code> - Display only the themes created by people using Amazon Quick Sight.</p> </li> <li> <p> <code>QUICKSIGHT</code> - Display only the starting themes defined by Quick Sight.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThemesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListThemesRequest:
    out: ListThemesRequest = {}  # type: ignore[typeddict-item]
    return out
