"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketAbacRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name


class GetBucketAbacRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The name of the general purpose bucket.</p>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID of the general purpose bucket's owner. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetBucketAbacRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetBucketAbacRequest:
    out: GetBucketAbacRequest = {}  # type: ignore[typeddict-item]
    return out
