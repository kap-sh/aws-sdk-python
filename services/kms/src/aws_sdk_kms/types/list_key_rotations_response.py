"""Generated from Smithy shape ``com.amazonaws.kms#ListKeyRotationsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.boolean_type
    import aws_sdk_kms.types.marker_type
    import aws_sdk_kms.types.rotations_list


class ListKeyRotationsResponse(TypedDict):
    rotations: NotRequired["aws_sdk_kms.types.rotations_list.RotationsList"]
    """<p>A list of completed key material rotations. When the optional input parameter <code>IncludeKeyMaterial</code> is specified with a value of <code>ALL_KEY_MATERIAL</code>, this list includes the first key material and any imported key material pending rotation.</p>"""
    next_marker: NotRequired["aws_sdk_kms.types.marker_type.MarkerType"]
    """<p>When <code>Truncated</code> is true, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent request.</p>"""
    truncated: "aws_sdk_kms.types.boolean_type.BooleanType"
    """<p>A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the <code>NextMarker</code> element in this response to the <code>Marker</code> parameter in a subsequent request.</p>"""
