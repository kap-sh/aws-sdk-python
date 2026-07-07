"""Generated from Smithy shape ``com.amazonaws.qapps#ListQAppsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qapps.types.instance_id
    import aws_sdk_qapps.types.page_limit
    import aws_sdk_qapps.types.pagination_token


class ListQAppsInput(TypedDict, closed=True):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    limit: NotRequired["aws_sdk_qapps.types.page_limit.PageLimit"]
    """<p>The maximum number of Q Apps to return in the response.</p>"""
    next_token: NotRequired["aws_sdk_qapps.types.pagination_token.PaginationToken"]
    """<p>The token to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQAppsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListQAppsInput:
    out: ListQAppsInput = {}  # type: ignore[typeddict-item]
    return out
