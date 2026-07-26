"""Generated from Smithy shape ``com.amazonaws.s3#ListBucketsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.buckets
    import capo_s3.types.next_token
    import capo_s3.types.owner
    import capo_s3.types.prefix


class ListBucketsOutput(TypedDict, closed=True):
    buckets: NotRequired["capo_s3.types.buckets.Buckets"]
    """<p>The list of buckets owned by the requester.</p>"""
    owner: NotRequired["capo_s3.types.owner.Owner"]
    """<p>The owner of the buckets listed.</p>"""
    continuation_token: NotRequired["capo_s3.types.next_token.NextToken"]
    """<p> <code>ContinuationToken</code> is included in the response when there are more buckets that can be listed with pagination. The next <code>ListBuckets</code> request to Amazon S3 can be continued with this <code>ContinuationToken</code>. <code>ContinuationToken</code> is obfuscated and is not a real bucket.</p>"""
    prefix: NotRequired["capo_s3.types.prefix.Prefix"]
    """<p>If <code>Prefix</code> was sent with the request, it is included in the response.</p> <p>All bucket names in the response begin with the specified bucket name prefix.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListBucketsOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "buckets" in value:
        import capo_s3.types.buckets

        capo_s3.types.buckets.serialize_xml(value["buckets"], el, "Buckets")
    if "owner" in value:
        import capo_s3.types.owner

        capo_s3.types.owner.serialize_xml(value["owner"], el, "Owner")
    if "continuation_token" in value:
        SubElement(el, "ContinuationToken").text = str(value["continuation_token"])
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])


def deserialize_xml(el: Element) -> ListBucketsOutput:
    out: ListBucketsOutput = {}  # type: ignore[typeddict-item]
    child_buckets = el.find("Buckets")
    if child_buckets is not None:
        import capo_s3.types.buckets

        out["buckets"] = capo_s3.types.buckets.deserialize_xml(child_buckets)
    child_owner = el.find("Owner")
    if child_owner is not None:
        import capo_s3.types.owner

        out["owner"] = capo_s3.types.owner.deserialize_xml(child_owner)
    child_continuation_token = el.find("ContinuationToken")
    if child_continuation_token is not None:
        out["continuation_token"] = str(child_continuation_token.text or "")
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    return out
