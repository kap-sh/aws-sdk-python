"""Generated from Smithy shape ``com.amazonaws.s3#PublicAccessBlockConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.setting


class PublicAccessBlockConfiguration(TypedDict, closed=True):
    block_public_acls: NotRequired["capo_s3.types.setting.Setting"]
    """<p>Specifies whether Amazon S3 should block public access control lists (ACLs) for this bucket and objects in this bucket. Setting this element to <code>TRUE</code> causes the following behavior:</p> <ul> <li> <p>PUT Bucket ACL and PUT Object ACL calls fail if the specified ACL is public.</p> </li> <li> <p>PUT Object calls fail if the request includes a public ACL.</p> </li> <li> <p>PUT Bucket calls fail if the request includes a public ACL.</p> </li> </ul> <p>Enabling this setting doesn't affect existing policies or ACLs.</p>"""
    ignore_public_acls: NotRequired["capo_s3.types.setting.Setting"]
    """<p>Specifies whether Amazon S3 should ignore public ACLs for this bucket and objects in this bucket. Setting this element to <code>TRUE</code> causes Amazon S3 to ignore all public ACLs on this bucket and objects in this bucket.</p> <p>Enabling this setting doesn't affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set.</p>"""
    block_public_policy: NotRequired["capo_s3.types.setting.Setting"]
    """<p>Specifies whether Amazon S3 should block public bucket policies for this bucket. Setting this element to <code>TRUE</code> causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access. </p> <p>Enabling this setting doesn't affect existing bucket policies.</p>"""
    restrict_public_buckets: NotRequired["capo_s3.types.setting.Setting"]
    """<p>Specifies whether Amazon S3 should restrict public bucket policies for this bucket. Setting this element to <code>TRUE</code> restricts access to this bucket to only Amazon Web Services service principals and authorized users within this account if the bucket has a public policy.</p> <p>Enabling this setting doesn't affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PublicAccessBlockConfiguration, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "block_public_acls" in value:
        SubElement(el, "BlockPublicAcls").text = (
            "true" if value["block_public_acls"] else "false"
        )
    if "ignore_public_acls" in value:
        SubElement(el, "IgnorePublicAcls").text = (
            "true" if value["ignore_public_acls"] else "false"
        )
    if "block_public_policy" in value:
        SubElement(el, "BlockPublicPolicy").text = (
            "true" if value["block_public_policy"] else "false"
        )
    if "restrict_public_buckets" in value:
        SubElement(el, "RestrictPublicBuckets").text = (
            "true" if value["restrict_public_buckets"] else "false"
        )


def deserialize_xml(el: Element) -> PublicAccessBlockConfiguration:
    out: PublicAccessBlockConfiguration = {}  # type: ignore[typeddict-item]
    child_block_public_acls = el.find("BlockPublicAcls")
    if child_block_public_acls is not None:
        out["block_public_acls"] = (
            child_block_public_acls.text or ""
        ).lower() == "true"
    child_ignore_public_acls = el.find("IgnorePublicAcls")
    if child_ignore_public_acls is not None:
        out["ignore_public_acls"] = (
            child_ignore_public_acls.text or ""
        ).lower() == "true"
    child_block_public_policy = el.find("BlockPublicPolicy")
    if child_block_public_policy is not None:
        out["block_public_policy"] = (
            child_block_public_policy.text or ""
        ).lower() == "true"
    child_restrict_public_buckets = el.find("RestrictPublicBuckets")
    if child_restrict_public_buckets is not None:
        out["restrict_public_buckets"] = (
            child_restrict_public_buckets.text or ""
        ).lower() == "true"
    return out
