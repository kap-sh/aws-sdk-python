"""Generated from Smithy shape ``com.amazonaws.s3control#PublicAccessBlockConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.setting


class PublicAccessBlockConfiguration(TypedDict, closed=True):
    block_public_acls: "capo_s3_control.types.setting.Setting"
    """<p>Specifies whether Amazon S3 should block public access control lists (ACLs) for buckets in this account. Setting this element to <code>TRUE</code> causes the following behavior:</p> <ul> <li> <p> <code>PutBucketAcl</code> and <code>PutObjectAcl</code> calls fail if the specified ACL is public.</p> </li> <li> <p>PUT Object calls fail if the request includes a public ACL.</p> </li> <li> <p>PUT Bucket calls fail if the request includes a public ACL.</p> </li> </ul> <p>Enabling this setting doesn't affect existing policies or ACLs.</p> <p>This property is not supported for Amazon S3 on Outposts.</p>"""
    ignore_public_acls: "capo_s3_control.types.setting.Setting"
    """<p>Specifies whether Amazon S3 should ignore public ACLs for buckets in this account. Setting this element to <code>TRUE</code> causes Amazon S3 to ignore all public ACLs on buckets in this account and any objects that they contain. </p> <p>Enabling this setting doesn't affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set.</p> <p>This property is not supported for Amazon S3 on Outposts.</p>"""
    block_public_policy: "capo_s3_control.types.setting.Setting"
    """<p>Specifies whether Amazon S3 should block public bucket policies for buckets in this account. Setting this element to <code>TRUE</code> causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access. </p> <p>Enabling this setting doesn't affect existing bucket policies.</p> <p>This property is not supported for Amazon S3 on Outposts.</p>"""
    restrict_public_buckets: "capo_s3_control.types.setting.Setting"
    """<p>Specifies whether Amazon S3 should restrict public bucket policies for buckets in this account. Setting this element to <code>TRUE</code> restricts access to buckets with public policies to only Amazon Web Services service principals and authorized users within this account.</p> <p>Enabling this setting doesn't affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked.</p> <p>This property is not supported for Amazon S3 on Outposts.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PublicAccessBlockConfiguration, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "BlockPublicAcls").text = (
        "true" if value.get("block_public_acls", False) else "false"
    )
    SubElement(el, "IgnorePublicAcls").text = (
        "true" if value.get("ignore_public_acls", False) else "false"
    )
    SubElement(el, "BlockPublicPolicy").text = (
        "true" if value.get("block_public_policy", False) else "false"
    )
    SubElement(el, "RestrictPublicBuckets").text = (
        "true" if value.get("restrict_public_buckets", False) else "false"
    )


def deserialize_xml(el: Element) -> PublicAccessBlockConfiguration:
    out: PublicAccessBlockConfiguration = {}  # type: ignore[typeddict-item]
    child_block_public_acls = el.find("BlockPublicAcls")
    if child_block_public_acls is not None:
        out["block_public_acls"] = (
            child_block_public_acls.text or ""
        ).lower() == "true"
    else:
        out["block_public_acls"] = False
    child_ignore_public_acls = el.find("IgnorePublicAcls")
    if child_ignore_public_acls is not None:
        out["ignore_public_acls"] = (
            child_ignore_public_acls.text or ""
        ).lower() == "true"
    else:
        out["ignore_public_acls"] = False
    child_block_public_policy = el.find("BlockPublicPolicy")
    if child_block_public_policy is not None:
        out["block_public_policy"] = (
            child_block_public_policy.text or ""
        ).lower() == "true"
    else:
        out["block_public_policy"] = False
    child_restrict_public_buckets = el.find("RestrictPublicBuckets")
    if child_restrict_public_buckets is not None:
        out["restrict_public_buckets"] = (
            child_restrict_public_buckets.text or ""
        ).lower() == "true"
    else:
        out["restrict_public_buckets"] = False
    return out
