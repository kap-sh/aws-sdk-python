"""Generated from Smithy shape ``com.amazonaws.macie2#BlockPublicAccess``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__boolean


class BlockPublicAccess(TypedDict):
    block_public_acls: NotRequired["aws_sdk_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether Amazon S3 blocks public access control lists (ACLs) for the bucket and objects in the bucket.</p>"""
    block_public_policy: NotRequired["aws_sdk_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether Amazon S3 blocks public bucket policies for the bucket.</p>"""
    ignore_public_acls: NotRequired["aws_sdk_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether Amazon S3 ignores public ACLs for the bucket and objects in the bucket.</p>"""
    restrict_public_buckets: NotRequired["aws_sdk_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether Amazon S3 restricts public bucket policies for the bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BlockPublicAccess) -> dict:
    out: dict = {}
    if "block_public_acls" in value:
        out["blockPublicAcls"] = value["block_public_acls"]
    if "block_public_policy" in value:
        out["blockPublicPolicy"] = value["block_public_policy"]
    if "ignore_public_acls" in value:
        out["ignorePublicAcls"] = value["ignore_public_acls"]
    if "restrict_public_buckets" in value:
        out["restrictPublicBuckets"] = value["restrict_public_buckets"]
    return out


def deserialize_json(data: dict) -> BlockPublicAccess:
    out: BlockPublicAccess = {}  # type: ignore[typeddict-item]
    if "blockPublicAcls" in data:
        out["block_public_acls"] = data["blockPublicAcls"]
    if "blockPublicPolicy" in data:
        out["block_public_policy"] = data["blockPublicPolicy"]
    if "ignorePublicAcls" in data:
        out["ignore_public_acls"] = data["ignorePublicAcls"]
    if "restrictPublicBuckets" in data:
        out["restrict_public_buckets"] = data["restrictPublicBuckets"]
    return out
