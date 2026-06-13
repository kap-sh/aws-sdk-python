"""Generated from Smithy shape ``com.amazonaws.entityresolution#ListIdNamespacesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.next_token


class ListIdNamespacesInput(TypedDict):
    next_token: NotRequired["aws_sdk_entityresolution.types.next_token.NextToken"]
    """<p>The pagination token from the previous API call.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of <code>IdNamespace</code> objects returned per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdNamespacesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListIdNamespacesInput:
    out: ListIdNamespacesInput = {}  # type: ignore[typeddict-item]
    return out
