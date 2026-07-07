"""Generated from Smithy shape ``com.amazonaws.lambda#ListFunctionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.function_version
    import aws_sdk_lambda.types.master_region
    import aws_sdk_lambda.types.max_list_items
    import aws_sdk_lambda.types.string


class ListFunctionsRequest(TypedDict, closed=True):
    master_region: NotRequired["aws_sdk_lambda.types.master_region.MasterRegion"]
    """<p>For Lambda@Edge functions, the Amazon Web Services Region of the master function. For example, <code>us-east-1</code> filters the list of functions to include only Lambda@Edge functions replicated from a master function in US East (N. Virginia). If specified, you must set <code>FunctionVersion</code> to <code>ALL</code>.</p>"""
    function_version: NotRequired[
        "aws_sdk_lambda.types.function_version.FunctionVersion"
    ]
    """<p>Set to <code>ALL</code> to include entries for all published versions of each function.</p>"""
    marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>"""
    max_items: NotRequired["aws_sdk_lambda.types.max_list_items.MaxListItems"]
    """<p>The maximum number of functions to return in the response. Note that <code>ListFunctions</code> returns a maximum of 50 items in each response, even if you set the number higher.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFunctionsRequest:
    out: ListFunctionsRequest = {}  # type: ignore[typeddict-item]
    return out
