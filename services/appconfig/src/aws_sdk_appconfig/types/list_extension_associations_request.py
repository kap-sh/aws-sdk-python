"""Generated from Smithy shape ``com.amazonaws.appconfig#ListExtensionAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.arn
    import aws_sdk_appconfig.types.identifier
    import aws_sdk_appconfig.types.integer
    import aws_sdk_appconfig.types.max_results
    import aws_sdk_appconfig.types.next_token


class ListExtensionAssociationsRequest(TypedDict):
    resource_identifier: NotRequired["aws_sdk_appconfig.types.arn.Arn"]
    """<p>The ARN of an application, configuration profile, or environment.</p>"""
    extension_identifier: NotRequired["aws_sdk_appconfig.types.identifier.Identifier"]
    """<p>The name, the ID, or the Amazon Resource Name (ARN) of the extension.</p>"""
    extension_version_number: NotRequired["aws_sdk_appconfig.types.integer.Integer"]
    """<p>The version number for the extension defined in the association.</p>"""
    max_results: NotRequired["aws_sdk_appconfig.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["aws_sdk_appconfig.types.next_token.NextToken"]
    """<p>A token to start the list. Use this token to get the next set of results or pass null to get the first set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExtensionAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListExtensionAssociationsRequest:
    out: ListExtensionAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
