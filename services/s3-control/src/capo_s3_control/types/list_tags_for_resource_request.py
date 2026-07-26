"""Generated from Smithy shape ``com.amazonaws.s3control#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.s3_resource_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p> The Amazon Web Services account ID of the resource owner. </p>"""
    resource_arn: "capo_s3_control.types.s3_resource_arn.S3ResourceArn"
    """<p> The Amazon Resource Name (ARN) of the S3 resource that you want to list tags for. The tagged resource can be a directory bucket, S3 Storage Lens group or S3 Access Grants instance, registered location, or grant. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListTagsForResourceRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
