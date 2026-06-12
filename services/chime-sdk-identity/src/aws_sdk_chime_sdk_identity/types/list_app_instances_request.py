"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ListAppInstancesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.max_results
    import aws_sdk_chime_sdk_identity.types.next_token


class ListAppInstancesRequest(TypedDict):
    max_results: NotRequired["aws_sdk_chime_sdk_identity.types.max_results.MaxResults"]
    """<p>The maximum number of <code>AppInstance</code>s that you want to return.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_identity.types.next_token.NextToken"]
    """<p>The token passed by previous API requests until you reach the maximum number of <code>AppInstances</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppInstancesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAppInstancesRequest:
    out: ListAppInstancesRequest = {}  # type: ignore[typeddict-item]
    return out
