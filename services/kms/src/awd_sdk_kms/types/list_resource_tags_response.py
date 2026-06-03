"""Generated from Smithy shape ``com.amazonaws.kms#ListResourceTagsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.boolean_type
    import awd_sdk_kms.types.marker_type
    import awd_sdk_kms.types.tag_list


class ListResourceTagsResponse(TypedDict):
    tags: NotRequired["awd_sdk_kms.types.tag_list.TagList"]
    """<p>A list of tags. Each tag consists of a tag key and a tag value.</p> <note> <p>Tagging or untagging a KMS key can allow or deny permission to the KMS key. For details, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/abac.html\">ABAC for KMS</a> in the <i>Key Management Service Developer Guide</i>.</p> </note>"""
    next_marker: NotRequired["awd_sdk_kms.types.marker_type.MarkerType"]
    """<p>When <code>Truncated</code> is true, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent request.</p> <p>Do not assume or infer any information from this value.</p>"""
    truncated: "awd_sdk_kms.types.boolean_type.BooleanType"
    """<p>A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the <code>NextMarker</code> element in this response to the <code>Marker</code> parameter in a subsequent request.</p>"""
