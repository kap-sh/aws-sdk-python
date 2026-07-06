"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ListImportFileTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.integer
    import aws_sdk_migrationhubstrategy.types.string


class ListImportFileTaskRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_migrationhubstrategy.types.string.String"]
    """<p> The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set <code>maxResults</code> to 10. You'll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10. </p>"""
    max_results: NotRequired["aws_sdk_migrationhubstrategy.types.integer.Integer"]
    """<p> The total number of items to return. The maximum value is 100. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImportFileTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListImportFileTaskRequest:
    out: ListImportFileTaskRequest = {}  # type: ignore[typeddict-item]
    return out
