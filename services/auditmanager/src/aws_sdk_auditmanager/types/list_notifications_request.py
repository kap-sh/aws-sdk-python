"""Generated from Smithy shape ``com.amazonaws.auditmanager#ListNotificationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.max_results
    import aws_sdk_auditmanager.types.token


class ListNotificationsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_auditmanager.types.token.Token"]
    """<p> The pagination token that's used to fetch the next set of results. </p>"""
    max_results: NotRequired["aws_sdk_auditmanager.types.max_results.MaxResults"]
    """<p> Represents the maximum number of results on a page or for an API request call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListNotificationsRequest:
    out: ListNotificationsRequest = {}  # type: ignore[typeddict-item]
    return out
