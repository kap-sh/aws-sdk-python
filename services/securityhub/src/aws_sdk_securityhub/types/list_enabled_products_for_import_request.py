"""Generated from Smithy shape ``com.amazonaws.securityhub#ListEnabledProductsForImportRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.max_results
    import aws_sdk_securityhub.types.next_token


class ListEnabledProductsForImportRequest(TypedDict):
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The token that is required for pagination. On your first call to the <code>ListEnabledProductsForImport</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>"""
    max_results: NotRequired["aws_sdk_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnabledProductsForImportRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEnabledProductsForImportRequest:
    out: ListEnabledProductsForImportRequest = {}  # type: ignore[typeddict-item]
    return out
