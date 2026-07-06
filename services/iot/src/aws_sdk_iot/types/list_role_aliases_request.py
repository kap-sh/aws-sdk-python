"""Generated from Smithy shape ``com.amazonaws.iot#ListRoleAliasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.ascending_order
    import aws_sdk_iot.types.marker
    import aws_sdk_iot.types.page_size


class ListRoleAliasesRequest(TypedDict, closed=True):
    page_size: NotRequired["aws_sdk_iot.types.page_size.PageSize"]
    """<p>The maximum number of results to return at one time.</p>"""
    marker: NotRequired["aws_sdk_iot.types.marker.Marker"]
    """<p>A marker used to get the next set of results.</p>"""
    ascending_order: "aws_sdk_iot.types.ascending_order.AscendingOrder"
    """<p>Return the list of role aliases in ascending alphabetical order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRoleAliasesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRoleAliasesRequest:
    out: ListRoleAliasesRequest = {}  # type: ignore[typeddict-item]
    return out
