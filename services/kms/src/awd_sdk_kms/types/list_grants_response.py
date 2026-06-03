"""Generated from Smithy shape ``com.amazonaws.kms#ListGrantsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.boolean_type
    import awd_sdk_kms.types.grant_list
    import awd_sdk_kms.types.marker_type


class ListGrantsResponse(TypedDict):
    grants: NotRequired["awd_sdk_kms.types.grant_list.GrantList"]
    """<p>A list of grants.</p>"""
    next_marker: NotRequired["awd_sdk_kms.types.marker_type.MarkerType"]
    """<p>When <code>Truncated</code> is true, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent request.</p>"""
    truncated: "awd_sdk_kms.types.boolean_type.BooleanType"
    """<p>A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the <code>NextMarker</code> element in this response to the <code>Marker</code> parameter in a subsequent request.</p>"""
