"""Generated from Smithy shape ``com.amazonaws.appconfig#ListExtensionAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.arn
    import capo_appconfig.types.identifier
    import capo_appconfig.types.integer
    import capo_appconfig.types.max_results
    import capo_appconfig.types.next_token


class ListExtensionAssociationsRequest(TypedDict, closed=True):
    resource_identifier: NotRequired["capo_appconfig.types.arn.Arn"]
    """<p>The ARN of an application, configuration profile, or environment.</p>"""
    extension_identifier: NotRequired["capo_appconfig.types.identifier.Identifier"]
    """<p>The name, the ID, or the Amazon Resource Name (ARN) of the extension.</p>"""
    extension_version_number: NotRequired["capo_appconfig.types.integer.Integer"]
    """<p>The version number for the extension defined in the association.</p>"""
    max_results: NotRequired["capo_appconfig.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_appconfig.types.next_token.NextToken"]
    """<p>A token to start the list. Use this token to get the next set of results or pass null to get the first set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExtensionAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListExtensionAssociationsRequest:
    out: ListExtensionAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
